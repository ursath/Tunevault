import Menu from '../../Components/Menu';
import '../../Style/BasicsSections.scss'
import Lupa from '../../Resources/search.js';

export default function Members() {
  return (
    <div className='BasicsMembers'>
      <Menu />
      <div className='HeaderMP'>
        <h1>Members</h1>
      </div>
      <div className="Search">
        <input className="InputSearch" placeholder='Who are you looking for?' type="text" id="searcher" />
        <Lupa size="20" color="white" />
      </div>
      <div class="BlackMP">
        <h1 className='TrendingTittle'>Trending Vaults</h1>
      </div>
    </div>
  )
}

