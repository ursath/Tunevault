import React, { Component } from 'react';
import axios from "axios";
import Modal from "./Components/Modal";
import '../css/LogIn.css'
import Menu from "./Components/Menu"

class LogIn extends Component {
  constructor(props) {
    super(props);
    this.state = {
        modal: true,
        users: [],
        activeItem: {
            id_user: '',
            user: '',
            bio: '',
            profileimg: '',
            location:'',
        }
    };
  }

  componentDidMount() {
    this.refreshList();
  }
  
  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  createUser = () => {
    const item = { id_user: "", user: "", bio: "", profile_img: "", location: ""};
    this.setState({ activeItem: item,  modal: !this.state.modal });
  };

  refreshList = () => {
    axios
      .get("/api/profile/")
      .then((res) => this.setState({ users: res.data }))
      .catch((err) => console.log(err));
  };

  handleSubmit = (item) => {
    this.toggle();

    if (item.id) {
      // mensaje de error (ya existe el usuario)
      return;
    }
    axios
      .post("/api/profile/", item)  
      .then((res) => this.refreshList());
  };


  render() {
    const { activeItem, modal } = this.state;
    return (
   
      <div>
      <Menu />
      <Modal
        isOpen={modal}
        toggle={() => this.setState({ modal: !modal })}
        activeItem={activeItem}
        onSave={this.handleSubmit}
      />
    </div>

    );
  }

}

export default LogIn;