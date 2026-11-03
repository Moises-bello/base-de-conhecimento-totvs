---
content_hash: 70e666c8104f7250d0501d632aab7810708325ff3507c9b4e15dbc7af55618e4
fetched_at: '2026-06-29T00:09:23.181498+00:00'
page_id: '422546062'
product: rm
source: tdn-rm
title: 12.1.20
type: documentation
url: https://tdn.totvs.com/display/LRM/12.1.20
version: 4
---

* [Ajustes no Layout para geração da DIRF no exercício 2018](http://tdn.totvs.com/pages/viewpage.action?pageId=422545867)

1. Na tela de parâmetros para geração da DIRF o campo "Identificador de estrutura do layout" apresentará o valor default "Q84FV63".
2. Foi criado o campo "Indicador de Entidade em que a união detém maioria do capital social sujeito a voto" este campo será apresentado Registro DECPJ campo 12.
3. No registro BPFDEC foi criado o campo (05) Indicador de identificação do alimentando e (06) Indicador de identificação da previdência complementar estes campos serão gerados com o valor default "N".

* [Regra de geração dp campo no bloco P](http://tdn.totvs.com/pages/viewpage.action?pageId=422545977)

1
incomplete
 No encerramento do tributo, buscar o COD\_CTA de acordo com as regras atuais que implementamos para os demais registros.

* [Ajuste na rotina SPED Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=422545704)

1. [Registro C100](http://tdn.totvs.com/pages/viewpage.action?pageId=422545626) - Incluída as opções "3-Transporte Próprio por Conta do Remetente" e "4-Transporte Próprio por Conta do Destinatário" no campo 02-IND\_FRT selecionado na aba Transporte sub aba Identificação do Lançamento Fiscal.
2. [Registro C176](http://tdn.totvs.com/pages/viewpage.action?pageId=422545977) - Novo código do motivo do ressarcimento "5-Exportação" do campo 02-COD\_MOT\_RES, informado na aba Referência da Situação Tributária do Lançamento Fiscal.
3. [Registro D100](http://tdn.totvs.com/pages/viewpage.action?pageId=422545626) - Registro passa a ser gerado para os tipos de documento 67-Conhecimento de Transporte Eletrônico para Outros Serviços (CT-e OS) e 63-Bilhete de Passagem Eletrônico (BP-e)
4. [Registro E530](http://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+E) - Campo 2-IND\_DOC gerado com valor default igual a 3-Documento Fiscal quando houver documento referenciado no Lançamento Fiscal.
5. [Registro E531](http://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+E) - Gerado para Lançamentos Fiscal com código modelo de documento igual a 01 e 55 e quando possuir documentos relacionados.
6. [Registro K220](http://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+K) - Incluído o campo 2-QTD\_DEST.
7. [Registro 1100](http://tdn.totvs.com/pages/viewpage.action?pageId=422546011) - Novo tipo de documento "2-Declaração única de Exportação" no campo 02-IND\_DOC, informado no Lançamento Fiscal subpasta Exportação.

2
incomplete
Registros e campos incluídos no leiaute a partir do período de apuração de **janeiro de 2019**

1. Registro K290: Produção Conjunta - Ordem de Produção
2. Registro K291: Produção Conjunta - Itens Produzidos
3. Registro K292: Produção Conjunta – Insumos Consumidos
4. Registro K300: Produção Conjunta – Industrialização Efetuada por Terceiros
5. Registro K301: Produção Conjunta – Industrialização Efetuada por Terceiros - Itens Produzidos
6. Registro K302: Produção Conjunta – Industrialização Efetuada por Terceiros - Insumos Consumidos

* [Alteração do SPED Fiscal 2018 - Alteração no Lançamento Fiscal - Natureza de Exportação](http://tdn.totvs.com/pages/viewpage.action?pageId=64652032)

3
incomplete
Criado as opções de "**Declaração Única de Exportação Direta**" e "**Declaração Única de Exportação Indireta**" no campo Natureza Exportação no Lançamento Fiscal / Pasta Exportação.

4
incomplete
Criado a opção "**5 - Exportação**" no campo Motivo de Ressarcimento, no Lançamento Fiscal / Item / Pasta Referências.  
   
[Dados Fiscais do Produto - Sub Aba Tributação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938199)

5
incomplete
Criado o campo Produto sujeito Regulações Sanitárias, para que seja gerado **Grupo I80 -** Rastreabilidade de produto na NF-e 4.00. Inicialmente, o preenchimento deste grupo só é obrigatório no caso de medicamentos e produtos farmacêuticos. 

* [EFD - REINF](http://tdn.totvs.com/display/LRM/REINF)  
  ***Observação***: Alterações nos cadastros de log do cadastro de Filial, Dados Fiscais da Filial, Processo Judicial e Tributos Discutidos: Sempre que houver alteração nos cadastros que gerar registro de log, é necessário reintegrar esses dados com o TAF. Os dados só vão ser reintegrados quando houver LOG de alteração.



6
incomplete
No anexo [Parâmetro ECF - Escrituração Contábil Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=422545950) do cadastro da Filial, foi criado o campo DEREX - Declaração sobre utilização de recursos em moeda estrangeira. 



7
incomplete
Criado os campos Cliente Secret e Client Id que deverão ser preenchidos de acordo com a exigência da prefeitura do município.
