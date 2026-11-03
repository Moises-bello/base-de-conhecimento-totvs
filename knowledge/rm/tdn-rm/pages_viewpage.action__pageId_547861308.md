---
content_hash: 708092679be44e94e01631caf724e6b803ec4e6ba65179821eca097be50bf47a
fetched_at: '2026-06-29T00:10:42.829788+00:00'
page_id: '547861308'
product: rm
source: tdn-rm
title: 2.4 Remessa de Arquivo Bancário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547861308
version: 18
---

Consiste na geração de arquivos de remessa dos lançamentos a receber e envio à rede bancária, que oferece serviços diversificados de processamento, tais como: cobrança registrada, entre outros.  Neste contexto, a empresa estabelece um convênio com o Banco, que tem uma importante atuação garantindo agilidade e praticidade ao processo. 

É possível gerar a Remessa de Cobrança para os boletos que possuam o STATUS igual à:

* Em Aberto;
* Cancelado;
* Baixado;
* Baixado Parcialmente e
* Inativo.

No processo de geração de remessa para boletos com o STATUS Baixado, Baixados Parcialmente, Cancelados e Inativos, verifique antes se o campo COMANDO do boleto, está preenchido de acordo com as regras de cancelamento do registro junto ao banco.

falsePremissas

* Para gerar a remessa é necessário que o usuário tenha permissão de acesso ao Segmento Integração;
* É necessário também que o layout do relatório esteja disponível no segmento Integração/Gerador de Saídas;
* Este layout deverá ser informado como default no cadastro do Convênio, aba Remessa Bancária, para a Cobrança Eletrônica e/ou para Cobrança Eletrônica PIX;
* Realizar o [cadastro de Cobrança Eletrônica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042156613-RM-FIN-Como-incluir-um-cadastro-banc%C3%A1rio-para-ser-utilizado-na-remessa-de-Cobran%C3%A7a-).

Os boletos devem ser registrados no Banco através do envio de arquivo bancário.

A seguir, o usuário deve acessar o Módulo Gestão Financeira para gerar o arquivo de remessa para registro dos lançamentos no Banco.

Segundo comunicado da Febraban, a partir de janeiro/2017, os boletos devem ser emitidos por cobrança registrada para que sejam aceitos pelos bancos. Desde 01/06/2015, a rede bancária deixou de ofertar o produto cobrança sem registro. Os novos contratos de cobrança oferecidos pelos bancos são apenas de cobrança registrada.

Acessar Menu: *TOTVS Gestão Financeira | Contas a Pagar/a Receber | Boleto | Executar o Filtro*

O usuário pode utilizar o filtro do Sistema para selecionar boletos desejados.

Após selecionar o filtro desejado, o Sistema listará os boletos. O usuário deve acessar a opção “*Processo | Remessa Cobrança Eletrônica*”.

Neste momento, o Sistema apresenta o assistente para geração da remessa bancaria:

**Remessa de Cobrança Eletrônica:** Informar o código do cadastro bancário;  
**Status de Remessa:** Preencher de acordo com o status do Remessa do Boleto selecionado;  
**Status do Boleto:** Preencher de acordo com o status do Boleto selecionado;

Atenção:

Para a remessa utilizando "status boleto" verifique antes se o campo COMANDO do boleto, está de acordo com as regras de cancelamento do registro junto ao Banco.

* **Pasta destino:** Preencher com o local onde deseja salvar o arquivo de remessa gerado;
* Mantenha a flag **'Salvar arquivo de remessa gerado no servidor de aplicação'** desmarcada. Caso o ambiente esteja configurado em N camadas e pretenda gravar os diversos arquivos gerados num único servidor, pode-se avaliar a possibilidade de habilitar tal opção.

Clique  em Avançar e depois em Executar para concluir a operação.

Após a remessa, os campos STATUS.CNAB dos Lançamentos e o Status da Remessa do Boleto serão atualizados para "*Remetido*".

falseQuitação dos títulos pelos Clientes

O Banco envia à empresa um arquivo de retorno contendo informações de data de quitação,  valor pago e outras informações afins que caracterizam a ocorrência. A importação deste arquivo produzirá a baixa automática dos respectivos Lançamentos Financeiros. Mais detalhes: [Retorno bancário](https://tdn.totvs.com/pages/viewpage.action?pageId=547861439).

Cancelamento da Remessa

O cancelamento da remessa de Cobrança é processado pela visão de Boletos. Ao realizar processo de cancelamento da remessa, o sistema irá limpar automaticamente o código de barras do boleto. Dessa forma, quando o boleto for remetido novamente ao banco, o Código de Barras poderá ser gerado novamente. Após o cancelamento da remessa de Cobrança PIX, será apagado o QR Code, o Link e atualizado o Status da Remessa do PIX do boleto.

Veja também

* [Cross Segmentos - BackOffice Linha RM - FIN - Como gerar a Remessa de Cobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041637774-Cross-Segmentos-Backoffice-Linha-RM-FIN-Como-gerar-a-Remessa-de-Cobran%C3%A7a)
* [FIN - Cobrança Eletrônica](https://tdn.totvs.com/pages/viewpage.action?pageId=421388722)
* [Gerando um arquivo de remessa de Cobrança Eletrônica](https://tdn.totvs.com/pages/viewpage.action?pageId=421388630)
* [Remessa de Cobrança em Lote](https://tdn.totvs.com/pages/viewpage.action?pageId=421388723)
* [RM - FIN - Como incluir um cadastro bancário para ser utilizado na remessa de Cobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042156613-RM-FIN-Como-incluir-um-cadastro-banc%C3%A1rio-para-ser-utilizado-na-remessa-de-Cobran%C3%A7a-)
