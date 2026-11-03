---
content_hash: f30d9064a6c2bf9f9136017887d2742d9f93ca90fa7d540688c574c9624da78a
fetched_at: '2026-06-28T21:35:24.602801+00:00'
page_id: '270924988'
product: fluig
source: tdn-fluig
title: DES - Por que ocorre erro ao exportar ou movimentar formulário 'row size too
  large'?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270924988
version: 13
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** Todas as versões

# Ocorrência

Ao tentar exportar um novo formulário para a plataforma ou movimentar uma solicitação, os erros são apresentados da seguintes formas:

javajava 8126). Changing some columns to TEXT or BLOB or using ROW\_FORMAT=DYNAMIC or ROW\_FORMAT=COMPRESSED may help. In current row format, BLOB prefix of 768 bytes is stored inline.]]>

# Solução

Identificamos que essa situação ocorre em dois cenários, sendo o primeiro na exportação de formulário devido a quantidade de campos contidos no mesmo, com isto, o banco restringe a criação da tabela do formulário (metalista). O segundo cenário trata-se da movimentação de solicitações, onde o número de caracteres informados ultrapassa o limite do banco e acaba por restringir o envio das informações.

Há uma medida de contorno, a qual poderá ser adotada, mas não é assegurado em todos os casos que a mesma solucionará o incidente, cabe ressaltar que essa limitação é do próprio banco de dados e não uma limitação do produto. A medida consiste em alterar os parâmetros de limitações do MySQL. Para realizar o procedimento, basta inserir (ou alterar) as seguintes chaves no arquivo **my.ini (em Windows)** ou **my.cnf (em Linux):**

java

Em seguida, é necessário reiniciar o serviço do banco de dados para que as alterações entrem em vigor.

Caso o incidente persista após a alteração dos parâmetros, aconselhamos que seja implementando em seu diagrama o uso de um [Subprocesso](https://tdn.totvs.com/display/public/HF/Configurar+atividades+e+fluxos#Configuraratividadesefluxos-ConfigurarSubprocesso), visando dividir o formulário, seja para sanar a questão do número de campos inseridos no mesmo ou o número de informações a serem enviadas durante a movimentação de uma solicitação.
