---
content_hash: 439d11e74c17bf1fa5d12692de233b53f25f5dd866f2fae03bf453be4c0ee0dd
fetched_at: '2026-06-29T00:11:07.049591+00:00'
page_id: '638715240'
product: rm
source: tdn-rm
title: S-2231 - Cessão/Exercício em Outro Órgão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=638715240
version: 61
---

false

**A partir das Versões:**

* **12.1.31.238**
* **12.1.32.173**
* **12.1.33.105**
* **e Superiores**

# Objetivo:

---

O objetivo deste documento é apresentar a geração do evento  S-2231 - Cessão/Exercício em Outro Órgão.

Este evento é utilizado pelo cedente, declarante do vínculo de origem do trabalhador, para informar o início e término de cessão/exercício de trabalhador em outro órgão e suas eventuais alterações. Caso a cessão/exercício em outro órgão abranger mais de um vínculo do trabalhador no declarante, é necessário o envio do evento para cada um deles.

**Quem está obrigado**: o declarante cedente do trabalhador, toda vez que o trabalhador for exercer a sua atividade em outro declarante tendo a existência do ato de cessão ou não.

---

11ParametrizaçãoParametrização

Foi necessário criação de campos no cadastro de afastamento para atender ao leiaute, e para a liberação desses campos é necessário a execução do script pelo aplicativo RM.Atualizador.exe

Acessar o parametrizador e selecionar o leiaute S-1.0.

**Atenção**: O evento S-2231 somente está disponível a partir do leiaute S-1.0

Após a execução do script será disponibilizado no cadastro de afastamento os campos abaixo:

**Atenção:** Veja mais detalhes sobre esses campos em .

2Geração do evento S-2231Geração do evento S-2231

A partir do leiaute S-1.0 o evento S-2231 foi disponibilizado para que, toda vez que o trabalhador for exercer a sua atividade em outro declarante, o declarante cedente do trabalhador comunique ao eSocial.

Abaixo iremos demonstrar as duas possíveis situações com alguns exemplos.

23-1Cessão antes vigência do S-2231Cessão antes vigência do S-2231

Os exemplos abaixo são de cadastros de cessões feitos antes da alteração do leiaute para o S-1.0, com evento de início da cessão enviado no S-2230.

ExemplosExemplo 1Exemplo 1

**Funcionário cedido com afastamento pela Previdência**

1) Neste exemplo o afastamento do tipo K-Cessão/Requisição já encontra-se cadastrado no sistema.

2) O afastamento foi enviado ao RET no evento S-2230, devido ainda está no leiaute 2.5.

3) Após alterar para o leiaute S-1.0 (vide aba Parametrização neste documento), o funcionário afasta pela Previdência, neste caso antes de cadastrar o inicio do afastamento pela Previdência deverá finalizar a Cessão, informando como data fim um dia antes do inicio do afastamento pela Previdência e marcar o parâmetro "Não Gerar Gatilho de Término da Cessão".

No exemplo abaixo o Funcionário tem a cessão iniciada em 01/02/2021 e teve um afastamento pela Previdência no período de 16/02/2021 a 25/02/2021:

**Observação**: Ao marcar este parâmetro o sistema não gera o encerramento da cessão.

4) Após informar o fim da cessão, deverá realizar a inclusão do afastamento pela Previdência:

5) Após cadastrar o afastamento pela Previdência informando o inicio e o fim, deverá cadastrar a Cessão novamente com inicio um dia após o término do afastamento pela Previdência

Isso é necessário para que o funcionário continue cedido no produto de Folha de Pagamento e para que seja gerado o evento S-2231.

**Observações:**

1. Conforme regra do MOS regra 1.5. do evento S-2231 – Cessão/Exercício em outro Órgão, a data de início do S-2231 será o dia seguinte após o término do afastamento enviado pelo S-2230, ou seja, a data de início do S-2231 a ser considerada será a do campo Data Inicio Afastamento. Desta forma, **não deverá ser preenchido o campo "Data Início Continuidade Afast. Cessão"**.

6) Preencher os dados da aba eSocial

7) Após as inclusões acima, serão gerados os eventos:

* Evento S-2230 de término da cessão;
* Evento S-2230 com a inclusão do afastamento pela Previdência;
* Evento S-2231 com a inclusão da cessão.

**Observação:** Conforme regra supracitada, a tag <dtIniCessao> foi gerada conforme campo Data Início Afastamento, ou seja, um dia após o término do afastamento (tipo "P").

Exemplo 2Exemplo 2

**Encerramento da cessão**

1) Neste exemplo o afastamento do tipo "K-Cedido/Requisição" já encontra-se cadastrado no sistema.

2) O afastamento será enviado no evento S-2230:

3) Após alterar para o leiaute S-1.0 (vide aba Parametrização neste documento), acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários e preencha o fim da cessão:

4) Será gerado o evento S-2230 de término, conforme abaixo:

3-2Cessão após vigência do S-2231Afastamento após vigência do S-2231

Os exemplos abaixo referem-se a situação onde o funcionário é cedido após a vigência do evento S-2231.

Exemplos1Exemplo 1

**Início da Cessão**

1) Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários e realize o cadastro do afastamento:

2) Após salvar, acesse Anexos | Históricos | Histórico de Afastamentos:

3) Deverá editar o afastamento e cadastrar os dados necessários na aba eSocial.

4) Será gerado o evento S-2231 referente ao Inicio da Cessão:

2Exemplo 2

**Encerramento da cessão**

1) Neste exemplo o afastamento do tipo "K-Cedido/Requisição" já encontra-se cadastrado no sistema.

2) O afastamento será enviado no evento S-2231:

3)  Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários e preencha o fim da cessão:

4) Será gerado o evento S-2231 de término, conforme abaixo:

3Exemplo 3

**Funcionário cedido com afastamento pela Previdência**

1) Neste exemplo o afastamento do tipo "K-Cessão/Requisição" já encontra-se cadastrado no sistema.

2) A cessão já foi enviada para o RET no evento S-2231.

3) Antes de cadastrar o início do afastamento pela Previdência, deverá finalizar a cessão informando como data fim um dia antes do início do afastamento pela Previdência e marcar o parâmetro "Não Gerar Gatilho de Término da Cessão". Esse processo é necessário pois o histórico de afastamento não permite intercessão de datas, contudo, não deve ser gerado S-2231 de término, já que o funcionário continuará cedido para outra empresa.

No exemplo abaixo, o funcionário tem a cessão iniciada em 01/02/2021 e teve um afastamento pela Previdência no período de 21/02/2021 a 02/03/2021:

**Observação**: Ao marcar este parâmetro o sistema não gera o encerramento da cessão (S-2231 de término).

4) Após informar o fim da cessão, deverá realizar a inclusão do afastamento pela Previdência:

5) Informando o fim do afastamento pela Previdência, o usuário deverá retorna com o cadastro da cessão no histórico de afastamento do funcionário e preencher o parâmetro "Data Início Continuidade Afast. Cessão" vinculando ao afastamento inicial da cessão (Data Início Afastamento da cessão anterior).

Esse processo é necessário para que não seja gerado um novo S-2231 de inclusão, já que a cessão do funcionário para outra empresa não foi interrompido, ou seja, o S-2231 de inclusão gerado anteriormente continuou válido no governo. 

6) Ao informar o campo "Data Início Continuidade Afast. Cessão", o registro do histórico será considerado "filho" do registro de afastamento da cessão inicial. Desta forma, sempre que for gerado o XML (retificação, alteração, etc) deverá utilizar o registro de afastamento "pai" (registro inicial da cessão). No registro "filho", os dados do Trabalhador Cedido presentes na aba eSocial ficarão desabilitados.

7) Após as inclusões acima, na fila de evento terão os gatilhos abaixo:
