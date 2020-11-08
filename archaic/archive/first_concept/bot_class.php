<?php
class Bot{
	private $id;
	private $user;
	private $email;
	private $pword;
	private $listtofollow;

	public function getId(){
		return $this->id;
	}
	public function getUser(){
		return $this->user;
	}
	public function getPword(){
		return $this->pword;
	}
	public function getListtofollow(){
		return $this->listtofollow;
	}
	public function getEmail(){
		return $this->email;
	}

	public function __construct($str){
		if(strlen($str) >= 1){
			$bot_info = explode('/', $str);
			$this->id = $bot_info[0];
			$this->user = $bot_info[1];
			$this->email = $bot_info[2];
			$this->pword = $bot_info[3];
			$this->listtofollow = $bot_info[4];
		}
	}

	public function toArray(){
		$bot_arr = array(
			"ID"=>$this->getId(), "EMAIL"=>$this->getEmail(), "USUARIO"=>$this->getUser(), "PASSWORD"=>$this->getPword(), "LISTA DE ORDENES"=>$this->getListtofollow(),
		);
		return $bot_arr;
	}
}
?>
