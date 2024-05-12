//SPDX-License-Identifier: MIT

pragma solidity ^0.8.19;

contract xTree {
    string name;                // Nombre
    address person;             // Dirección de la persona
    string fam_memmory;         // Memorias de la familia
    string personal_memmory;    // Memorias personales
    address [] public spouse;   // Cónyuges
    address [] public sons;     // Hijos

    constructor(address _person, string memory _name, address _spouse) {
        person = _person;
        name = _name;
        spouse.push(_spouse);
    }

    function addSon(address _son) public {
        require(msg.sender == person, "Not authorized to execute this function.");
        sons.push(_son);
    }

    function addSpouse(address _spouse) public {
        require(msg.sender == person, "Not authorized to execute this function.");
        spouse.push(_spouse);
    }

    function getName() public view returns(string memory){
        return name;
    }

    function getSons()  public view returns (address [] memory) {
        return sons;
    }

    function getSpouse()  public view returns (address [] memory) {
        return spouse;
    }
}