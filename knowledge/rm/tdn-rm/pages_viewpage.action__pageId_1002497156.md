---
content_hash: 340eb316dd82c6f5f7b3a5c01aae607385f6b896a6c69d5e7903a534ae15e11a
fetched_at: '2026-06-29T00:05:45.039640+00:00'
page_id: '1002497156'
product: rm
source: tdn-rm
title: Integração TOTVS Gestão Hospitalar X Impressora unitarizadora OPUSPAC VideoJet
  6230/6330/6530
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1002497156
version: 7
---

opuspacvisaoVisão Geral

A integração do Totvs Gestão Hospitalar oferece nativamente compatibilidade com a impressora  unitarizadora **VideoJet (6230/6330/6530)** da empresa OpusPac (<https://opuspac.com/solucoes/>) , de forma que, ao enviar os dados de impressão com o layout adequado (por meio do IP e porta da impressora), a Opuspac reconhece e executa automaticamente a impressão das etiquetas de medicamentos por doses individuais.

**O Layout de impressão é personalizado por Produto.**

A **VideoJet (6230/6330/6530)** é uma impressoras para codificar dados variáveis em embalagens flexíveis.

Será disponibilizado nas versões 12.1.2602 e patch 12.1.2510, 12.1.2506

**Conceito de Unitarizar:**

Unitarizar é o processo de preparar os medicamentos na forma pronta, para ser administrados ao paciente**.**

Este processo é normalmente realizado na Farmácia do Hospital, Setor armazenagem de medicamentos ou Centro de Unitarização para vários hospitais, mas sempre ligado à responsabilidade e controle da Farmácia do Hospital. Unitarizar ou fazer o fracionamento de medicamentos é importante para centralizar o controle dos medicamentos na Farmácia Hospitalar e para diferenciar as embalagens. Também para colocar um código de barras do hospital**.**

**Benefícios alcançados com a integração com a impressora de etiquetas:**

Diminuição do tempo ocupado pela equipe de enfermagem para unitarizar nos andares e um menor desperdício.

Exemplo de impressora da empresa OpusPac, modelo Nina:

requisitosPré Requisitos para a integração

**Pré Requisitos para integração no Totvs Gestão Hospitalar**

**1 – Cadastro de Produto**

No cadastro do produto, anexo “Informações - Totvs Saúde”, possibilitar a configuração de qual layout da impressora será utilizado para a unitarização (Campo texto: nome do Layout).

**2 – Parâmetros Gerais do Gestão Hospitalar**

Informações de conexão com o equipamento por local de estoque: IP da impressora, Porta e Codificação (ASCII ou Unicode).

Pesquisar as informações de integração primeiro no Parâmetros Local de Estoque por Usuário.

Caso não encontre, será pesquisado em  Parâmetros Local de Estoque por Perfil.

E por último em Parâmetro Geral de Estoque 5/5.

**2.1 – Estoque / Local de Estoque – Permissão por usuário**

As informações de conexão da impressora se encontram na aba "Outros"

2.2 – Estoque / Local de Estoque – Permissão por perfil

As informações de conexão da impressora se encontram na aba "Outros"

2.3 - Estoque 5/5

**3 – Farmácia / Etiqueta de Código de Barras**

Tela de impressão das etiquetas - SauBarCodeLabelAction

Caso esteja parametrizado nos parâmetros gerais de Estoque a utilização da impressora OpusPac, será exibido um botão "Imprimir na impressora Unitarizadora" para o envio do comando para a impressora, considerando as informações de parametrização, layout do produto e informações do grid de saldo/lote do produto (da tela de emissão de etiquetas).

configConfigurações Técnicas da impressora

**Modelo de impressoras VideoJet (6230/6330/6530)**

**Protocolo de envio:** ASCII ou Unicode |CQI||SST||SLI|COMPRIMIDO|0|VALIDADE=31/01/2050|FABRICANTE=MEDICALCORPS|LOT E=00001|COD\_PRODUTO=001|NOME\_MED=DIPIRONA|DESCRICAO=DIPIRONA 500MG COMP|

**Destrinchamento da string**

 | = Delimitador de campos

|CQI| = (Clear Queue Item) limpa fila de impressão

|SST| = Pausa a impressão

|SLI| = identificador da mensagem (protocolo próprio da impressora)

|COMPRIMIDO| = Campo do Layout, é usado para identificar o layout na impressora

|0| = Quantidade, valor 0 não apresenta um número definido podendo ser impresso inúmeras vezes. VALIDADE=31/01/2050|FABRICANTE=MEDICALCORPS|LOTE=00001|COD\_PRODUTO= 001|NOME\_MED=DIPIRONA|DESCRICAO=DIPIRONA 500MG COMP| = Campos de transferência, |(campo layout) = (campo variável)|

**Modelo técnico da string:**

|CQI||SST||SLI|(Nome do layout)|(Quantidade)|(Campo 1=(Campo variável 1)|(Campo 2=(Campo variável 2)|(Campo 3=(Campo variável 3)|(Campo 4=(Campo variável 4)|(Campo 5=(Campo variável 5)|(Campo 6=(Campo variável 6)|...|

**Orientações para T.I** :

* Reserva de IP (IP deve ser estático) e das portas 1234 (envio de string do ERP à impressora) e 3001 (para layouts criados no Clarisoft) (para máquinas Opus Flag V.4, reservar a porta 55000 – usada para a interface da impressora);
* Informar-nos o IP reservado, máscara de rede e gateway;
* Seguirem a documentação presente, alinhando com os responsáveis pelo sistema para as parametrizações da string, de forma a haver comunicação eficiente entre o ERP e a impressora do equipamento;

##
