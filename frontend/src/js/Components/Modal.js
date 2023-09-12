import React, { Component } from "react";
import '../../css/Components/Modal.css';
import '../../css/Components/Basics.css';
import {
    Button,
    Modal,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label,
  } from "reactstrap";

export default class CustomModal extends Component {
    constructor(props) {
      super(props);
      this.state = {
        activeItem: this.props.activeItem,
      };
    }
  
    handleChange = (e) => {
      let { name, value } = e.target;
  
      if (e.target.type === "checkbox") {
        value = e.target.checked;
      }
  
      const activeItem = { ...this.state.activeItem, [name]: value };
  
      this.setState({ activeItem });
    };
  
    
    render() {
        const { toggle, onSave } = this.props;
      
        return (

            <Modal isOpen={true} toggle={toggle}>
              <ModalBody>
                <Form>
                  <FormGroup>
                    <Label for="user-id_user">User ID:</Label>
                    <Input
                      type="text"
                      id="user-id_user"
                      name="id_user"
                      value={this.state.activeItem.id_user}
                      onChange={this.handleChange}
                      placeholder="Enter ID"
                    />
                  </FormGroup>
                  <FormGroup>
                    <Label for="user-user">User name:</Label>
                    <Input
                      type="text"
                      id="user-user"
                      name="user"
                      value={this.state.activeItem.user}
                      onChange={this.handleChange}
                      placeholder="Enter your user name"
                    />
                  </FormGroup>
                  <FormGroup>
                    <Label for="user-username">Biography:</Label>
                    <Input
                      type="text"
                      id="user-bio"
                      name="bio"
                      value={this.state.activeItem.bio}
                      onChange={this.handleChange}
                      placeholder="Enter a biography"
                    />
                  </FormGroup>
                  <FormGroup>
                    <Label for="user-password">Profile Image</Label>
                    <Input
                      type="file"
                      id="user-img"
                      name="img"
                      value={this.state.activeItem.img}
                      onChange={this.handleChange}
                      placeholder="Enter a profile image"
                    />
                  </FormGroup>
                  <FormGroup>
                    <Label for="user-location">Location:</Label>
                    <Input
                      type="text"
                      id="user-location"
                      name="location"
                      value={this.state.activeItem.location}
                      onChange={this.handleChange}
                      placeholder="Enter your location"
                    />
                  </FormGroup>
                </Form>
              </ModalBody>
              <ModalFooter>
                <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                  Save
                </Button>
              </ModalFooter>
            </Modal>

        );
      }
      
  }