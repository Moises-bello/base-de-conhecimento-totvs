---
article_id: 4402791435031
category: Inspeção de Processos (SIGAQIP)
content_hash: e8f88c3767c2d3b21e1e479ec9143f0c46300b86164d8b890b2b9f7cd454b6c6
fetched_at: '2026-06-28T22:42:25.874987+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - O Lote informado já existe para esta
  Ordem de Produção, indique outro Lote
type: support-article
updated_at: '2026-04-24T17:57:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402791435031-Manufatura-Linha-Protheus-SIGAQIP-O-Lote-informado-j%C3%A1-existe-para-esta-Ordem-de-Produ%C3%A7%C3%A3o-indique-outro-Lote
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39993536375703) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
No módulo **SIGAPCP - Planejamento e Controle da Produção**, ao tentar efetuar um apontamento na rotina **MATA681 - Produção PCP Mod2** ocorre a mensagem **O Lote informado já existe para esta Ordem de Produção, indique outro Lote!**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**  
A mensagem **O Lote informado já existe para esta Ordem de Produção, indique outro Lote!** é um comportamento padrão quando existe integração do **SIGAPCP** com o módulo **SIGAQIP - Inspeção de Processos**.  
Quando a integração com o **SIGAQIP** está ativa, cada apontamento gera um registro na rotina **QIPA215 - Cadastro de Resultados** e posteriormente um laudo sendo aprovado ou rejeitado. Caso o Sistema permitisse registrar dois ou mais apontamentos do mesmo **Produto**, **Ordem de Produção** e **Lote**, iria gerar inconsistência em consultas futuras, pois o mesmo **Produto** e **Lote** poderiam ter laudos diferentes, sendo um aprovado e um rejeitado, por exemplo.  
Além disto, a chave primária da tabela **QPK - Insp. Processos - Avaliações** confirma que esta regra de negócio é necessária para consistência das informações:  
**QPK\_FILIAL+QPK\_OP+QPK\_LOTE+QPK\_NUMSER+QPK\_PRODUT+QPK\_REVI**  
  
Onde:  
**QPK\_FILIAL - Filial**  
**QPK\_OP - Ordem Produção**  
**QPK\_LOTE - Lote**  
**QPK\_NUMSER - Num de Série**  
**QPK\_PRODUT - Produto**  
**QPK\_REVI - Revisão**  
  
**Solução**  
Para gerar mais de uma inspeção por **OP - Ordem de Produção** utilizando apontamento parcial, é possível proceder de 3 formas:

1. Efetuar o apontamento total da **OP** gerando um único **Lote**, caso a inspeção aponte problemas todo o **Lote** será reprovado, ou;
2. Efetuar o apontamento parcial gerando um novo **Lote** para cada apontamento. Desta forma, caso algum **Lote** tenha problemas durante a inspeção apenas esse **Lote** será reprovado, ou;
3. Efetuar o apontamento informando **Lote** e **Sub-lote**.

**Observação**  
Caso o apontamento ocorra via rotina **SFCA314  - Apontamento da Produção Modelo 2**, para utilizar o **conceito de sub-lote**, será preciso habilitar o Ponto de Entrada [PE SCA314SBL Permitir preencher o sublote no programa SFCA314](https://tdn.totvs.com/display/public/PROT/PE+SCA314SBL+Permitir+preencher+o+sublote+no+programa+SFCA314) e o parâmetro **MV\_LOTEUNI - O conceito de LOTE UNICO devera ser utilizado para produtos c/rastreabilidade igual a LOTE?** com conteúdo igual a **T - True**.
