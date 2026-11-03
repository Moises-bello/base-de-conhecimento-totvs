---
article_id: 360011281992
category: RH - Arquivos Bancarios
content_hash: 010ad95690fd2a66f8eb267a776dcbb045ab2a61509bfe264e640defdce176b3
fetched_at: '2026-06-28T22:43:38.271144+00:00'
product: protheus
section_id: 360004833673
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar e gerar o arquivo de empréstimo
  consignado
type: support-article
updated_at: '2025-05-23T17:55:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011281992-RH-Linha-Protheus-GPE-Como-configurar-e-gerar-o-arquivo-de-empr%C3%A9stimo-consignado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32325767937559)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como configurar e gerar o arquivo de empréstimo consignado, a fim de ser enviado ao banco através da rotina GPEM700?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**O ambiente Gestão de Pessoal foi devidamente adequado para o controle dos dados enviados pelas instituições financeiras, efetuando o devido desconto das parcelas na folha de pagamento, além de gerar o arquivo para repasse dos resultados.

Esta comunicação bancária é feita através de arquivos em formato texto ".TXT", gerados com estrutura de acordo com o *layout* fornecido pela instituição, que deve ser devidamente cadastrado no ambiente Configurador.

**Antes de iniciar** a inclusão de um *layout* de arquivo, o[modelo de comunicação bancária](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/gpem700_modelo_de_comunicacao_bancaria_bra.htm)deve ser definido, conforme Manual de Instruções do banco, via ambiente Configurador.

1. Em arquivo, são relacionados os registros já existentes, classificados conforme [legenda;](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/gpem700_legenda_bra.htm)  
  
2. Selecione a opção "Incluir";  
  
É apresentada a janela que permite relacionar o *layout* do banco com a configuração do arquivo.

**3**. Preencha os campos conforme orientação a seguir;

* Banco/Nome: digite o código e o nome do banco para o qual será gerado o arquivo, e de onde é configurado o *layout* de arquivo.
* *Layout*: selecione o tipo de *layout* sobre o qual os dados do arquivo a ser gerado serão. considerados, de acordo com as opções disponíveis, sendo: CNAB Padrão / CNAB Modelo 2 / Sispag.
* Arquivo de configuração: selecione o arquivo de configuração que contém as especificações do *layout*, previamente cadastrado no ambiente Configurador. Clique na opção  para que seja apresentada a janela de seleção dos arquivos.

Nesta tela, na caixa de listagem "Listar apenas os arquivos do tipo:", selecione o tipo de arquivo de configuração que será utilizado, de acordo com *layout* selecionado, sendo: TXT / RET / REM / 2RE / PAG.  
Em seguida, selecione o arquivo de configuração a ser utilizado, e confirme.  
  
- Verba: clique em "Pesquisar"  para selecionar a verba em que serão lançados os valores do empréstimo na folha.

**4**. Informe as configurações de *layout*, conforme especificações do banco;

As próximas informações **são muito importantes para o correto tratamento das informações** enviadas pelo banco. Portanto, verifique o *layout* cadastrado no ambiente Configurador e preencha os campos conforme orientações.

* Rem/Ret: neste campo informe em que posição do *layout* o código de remessa ou de retorno deve ser apresentado no arquivo gerado.
* Tp.Pgto: neste campo informe em que posição do *layout* o código do tipo de pagamento deve ser apresentado no arquivo gerado.
* CPF: informe a posição em que o "CPF" do funcionário será gerado no arquivo.

Informações de Parcela(s)

* Parcela: informe a posição em que a parcela será gerada no arquivo, considerando o seguinte:  
    
  - Para arquivos de Manutenção da Consignação, que apresentem somente descontos mensais em folha, informe a posição do item "Número da Parcela".  
  - Para arquivos de Averbação da Consignação, que relaciona informações dos funcionários que solicitaram o empréstimo, informe a posição do item "Total de Parcelas".

Em ambos os casos, a posição do campo no *layout* é a mesma.

* Qtd.Consig: informe a posição em que a quantidade de parcelas que foram descontadas do funcionário será apresentada, cujo conteúdo será calculado pela Folha.
* Qtd.N.Consig: informe a posição em que a quantidade de parcelas que não foram descontadas do funcionário será apresentada, independentemente do(s) motivo(s), cujo conteúdo será calculado pela Folha.

Informações de valore(s)

* Valor: informe a posição em que o valor do empréstimo será gerado no arquivo, considerando o seguinte:  
    
  - Para arquivos de Manutenção da Consignação, informe a posição do item "Valor da Parcela"  
  - Para dos arquivos de Averbação da Consignação, informe a posição do item "Valor Total"

Em ambos os casos, a posição do campo no *layout* é a mesma.

* Total N. Consig: Informe a posição em que o valor referente à soma das parcelas descontadas dos funcionários será apresentado, cujo conteúdo será calculado pela Folha.

Informe a posição em que o valor referente às parcelas que não foram descontados dos funcionários, independentemente do(s) motivo(s), cujo conteúdo calculado pela Folha.

**5**. Informados os campos e a configuração do arquivo, confira-os e confirme;

**6**. Repita estes procedimentos para incluir todos os bancos necessários;

**7**. Criados os arquivos de configuração, os dados bancários que definirão o arquivo devem ser importados através da opção de menu "[Importar Dados](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/gpem700_importar_dados_bra.htm)";

**8**. Criados os arquivos de configuração e definidos os dados bancários do arquivo, as informações que comporão o arquivo devem ser gerados através da opção de menu "[Gerar Remessa](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/gpem700_gerar_remessa_bra.htm)".  
  
**Saiba Mais**  
[Página Centralizadora Arquivos Bancários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833673-RH-Arquivos-Bancarios)
