---
article_id: 360015138212
category: Contabilidade Gerencial - Intercompany
content_hash: a0d4a4639f89693e347b0984b228f393988cd331b34f2a50a7e49965094458a2
fetched_at: '2026-06-28T22:40:37.773949+00:00'
product: protheus
section_id: 1500001548902
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA290 - Intercompany
type: support-article
updated_at: '2024-08-13T14:27:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015138212-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA290-Intercompany
---

**Dúvida**Quais os procedimentos para usar a rotina CTBA290?  
  
**Ambiente**Protheus – Contabilidade – A partir da versão 11.80  
  
  
**Solução**O recurso Intercompany permite efetuar lançamentos contábeis entre filiais/empresas de forma automática. Efetiva o processamento dos lançamentos registrados no Cadastro Intercompany.

Para que os lançamentos de Intercompany sejam executados corretamente, é necessário:

* Habilitar o uso do campo "Intercompany" (CT2\_INTERC) na tabela de Lançamentos Contábeis;
* Através da rotina CTBA102 Identificar os lançamentos contábeis, informando “Sim” no campo
* Cadastrar as regras de Intercompany na opção "Cadastro Intercompany";
* Executar a rotina  "Miscelânea + Processamentos + Intercompany"

Para efetivar os lançamentos Intercompany:

1. Ao acessar a rotina Intercompany (menu Miscelânea), é apresentada uma mensagem de alerta informado que os arquivos associados a esta rotina não devem estar em uso por outras estações.  
Caso estejam e uso, é necessário que os usuários saiam do sistema.

2. Confirme a execução da rotina, quando todos os arquivos estiverem liberados.  
É apresentada a janela Lançamentos Intercompany, indicando que este programa transporta os lançamentos Intercompany.

3. Clique em Parâmetros, para configurar os parâmetros envolvidos no processamento, tais como: período, código do cadastramento Intercompany, tipo de histórico a ser utilizado (do lançamento contábil ou histórico padrão), atualiza saldos, moedas, tipo de saldo (real, previsto, gerencial,empenhado, pré-lançamento, etc.), entre outros.  
4. Configure os parâmetros conforme orientação do help de campo e confirme.  
5. Clique em Ok, para confirmar o processamento da rotina.

**Veja Mais**

[Intercompany (CTBA290 - SIGACTB)](https://tdn.totvs.com/pages/releaseview.action?pageId=340367154)

[Rateio entre Empresas](https://tdn.totvs.com/display/public/PROT/Rateio+entre+Empresas+--+113001)
