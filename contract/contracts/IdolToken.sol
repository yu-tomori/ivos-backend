pragma solidity 0.5.8;
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/ProjectOpenSea/opensea-creatures/contracts/Strings.sol";

// import "openzeppelin-solidity/contracts/token/ERC721/ERC721Full.sol";
// import "./Strings.sol";

contract IdolToken is ERC721Full {
    
    using Strings for string;

    constructor(string memory _name, string memory _symbol) ERC721Full(_name, _symbol) public {}
    
    struct Voice {
        address owner;
        uint256 totalSupply;
        uint256 issuedNum;
        uint256 price;
    }

    mapping (address => uint256[]) public ownedVoices;
    mapping (address => uint256) public balanceOfOwnedVoices;
    mapping (uint256 => Voice) public voices; // voiceId : Voice
    mapping (uint256 => uint256) public voiceIds; // tokenId : voiceId
    
    string baseUrl = "https://sample.com/voice/";

    // アイドルがトークンの設定をする
    // 音声ファイルID、最大発行料、金額
    function releaseVoice(uint256 _voiceId, uint256 _totalSupply, uint256 _price) public {
        Voice memory newVoice = Voice({
            owner: msg.sender,
            totalSupply: _totalSupply,
            issuedNum: 0,
            price: _price
        });
        voices[_voiceId] = newVoice;
        ownedVoices[msg.sender].push(_voiceId);
        balanceOfOwnedVoices[msg.sender]++;
    }

    function getVoice(uint256 _voiceId) public view returns(address, uint256, uint256, uint256) {
        Voice memory newVoice = voices[_voiceId];
        return ( newVoice.owner, newVoice.totalSupply, newVoice.issuedNum, newVoice.price);
    }

    // アイドルの音声IDに紐づくトークンの最大発行料
    function getTotalSupply(uint256 _voiceId) public view returns(uint256) {
        return voices[_voiceId].totalSupply;
    }

    // アイドルの音声IDに紐づくトークンのすでに発行されている数
    function getIssuedNum(uint256 _voiceId) public view returns(uint256) {
        return voices[_voiceId].issuedNum;
    }

    // アイドルの音声IDに紐づくトークンの価格
    function getPrice(uint256 _voiceId) public view returns(uint256) {
        return voices[_voiceId].price;
    }

    // ユーザーが購入する（発行）
    function mintVoice(uint256 _voiceId) public payable{
        
       Voice storage newVoice = voices[_voiceId];
       require(msg.value == newVoice.price);
       require(newVoice.issuedNum < newVoice.totalSupply);
       uint256 tokenId = totalSupply();
       _mint(msg.sender, tokenId);
       voiceIds[tokenId] = _voiceId;
       newVoice.issuedNum++;
       
      string memory uri = Strings.strConcat(baseUrl, Strings.uint2str(tokenId));
      _setTokenURI(tokenId, uri);
   }
}