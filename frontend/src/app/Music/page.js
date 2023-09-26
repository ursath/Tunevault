import Menu from '../../Components/Menu';
import '../../Style/Music.scss'
import Lupa from '../../Resources/search.js';

export default function Music() {
  return (
    <div className='BasicsMusic'>
      <Menu />
      <div className='HeaderMusic'>
        <h1>Music</h1>
      </div>
      <div className="Search">
        <input className="InputSearch" placeholder='What do you want to talk about?' type="text" id="searcher" />
        <Lupa size="20" color="white" />
      </div>
      <div class="Filters">
        <label className='Label'>FILTER BY</label>
        <select className='custom-select'>
          <option value="0">Genre</option>
          <option value="1">Disco</option>
          <option value="2">Rock</option>
          <option value="3">Classic</option>
          <option value="4">Reggaeton</option>
          <option value="5">Pop</option>
          <option value="6">Salsa</option>
        </select>
        <select className='custom-select'>
          <option value="0">Active</option>
          <option value="1">Trending</option>
          <option value="2">Emergent</option>
          <option value="3">New</option>
        </select>
      </div>
      <div class="BlackMusic">
        <h1 className='TrendingTittle'>Trending Vaults</h1>
      </div>
    </div>
  )
}

