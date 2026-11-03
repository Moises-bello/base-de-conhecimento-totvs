---
content_hash: 8d6db39906abb71012e07c83c87e6ad463638ac9a1e7a0f05ce9b031410ec61f
fetched_at: '2026-06-29T00:11:09.600339+00:00'
page_id: '640545308'
product: rm
source: tdn-rm
title: Alteração do algoritmo de Hash do RM (Bcrypt)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=640545308
version: 12
---

A partir da versão **12.1.34**, o RM terá a possibilidade de utilizar um novo algoritmo para geração de hashs (**Bcrypt**). - <https://github.com/BcryptNet/bcrypt.net>

A partir da versão **12.1.2410**, o RM passará a adotar o novo algoritmo **Bcrypt** como padrão para todos os clientes.

O Bcrypt foi escolhido pois ele cumpre todas as especificações levantadas para atender as necessidades do RM.

Essa ação visa aumentar o nível de segurança do armazenamento das senhas dos usuários.

Foi necessário atuar em duas ações principais:

1- Aumentar o tamanho do campo SENHA de 8 para 1000

2- Implementar a abstração, modificando o mínimo possível, visando diminuir os colaterais.

Após essa alteração o campo senha terá o seguinte formato, seguindo o padrão PHC (Password Hashing Competition) - <https://github.com/P-H-C/phc-string-format/blob/master/phc-sf-spec.md>

#P=False#PT=None#WF=10#HT=SHA256#HA=Bcrypt#V=4.0.2.0#H=$2a$10$y.SWHIgYl74q1fEKWMU5EObE7b52a3kS2jYxySEIfkbdKqZ1ort4S

### Parâmetro / Segurança

Armazenar a senha nesse formato permitirá ao RM modificar os parâmetros, caso seja necessário, para aumentar o nível de complexidade do hash no futuro, além de permitir o uso de outros algoritmos de forma transparente e conjunta.

### Atualização gradativa de senhas no banco de dados

A imagem abaixo, mostra o fluxo que irá promover a atualização gradativa dos hashs de senhas (a cada novo login o hash será atualizado):
