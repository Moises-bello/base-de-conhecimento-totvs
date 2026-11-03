---
article_id: 37708600917015
category: Financeiro - Baixas Automáticas a Pagar
content_hash: 59bfffde242c84ca4fb2b401d2cdeddd4cb02d267749a082d20968ca1abbe993
fetched_at: '2026-06-28T22:37:36.355890+00:00'
product: protheus
section_id: 35057495195543
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Retorno CNAB a pagar
  registra qual banco de pagamento na SE5
type: support-article
updated_at: '2026-01-16T10:06:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37708600917015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Retorno-CNAB-a-pagar-registra-qual-banco-de-pagamento-na-SE5
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37708584434199) Tempo aproximado para leitura: **00:05 min**

**Dúvida**  
No retorno do CNAB a Pagar (Modelo 2), qual a prioridade do sistema para definir o Banco, Agência e Conta que serão gravados no movimento bancário (SE5) no momento da baixa?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as Versões  
  
**Solução**

O processo de retorno de pagamento (CNAB Modelo 2 - 240 posições), o Protheus segue uma ordem de prioridade para determinar os dados bancários da baixa. O sistema avalia as configurações na seguinte sequência:

1. **Parâmetros de Bancos (FINA130):** Se os campos **Banco Oficial (EE\_CODOFI)**, **Agência Oficial (EE\_AGEOFI)** e **Conta Oficial (EE\_CTAOFI)** estiverem preenchidos no cadastro do banco correspondente, estes dados serão utilizados prioritariamente para a geração do movimento no SE5.
2. **Cabeçalho do Arquivo Retorno:** Caso os campos de "Conta Oficial" mencionados acima estejam em branco, o sistema utilizará as informações de Banco/Agência/Conta retornadas no arquivo enviado pelo banco.
3. **Perguntas da Rotina:** Se não houver informações nos parâmetros oficiais nem no arquivo, o sistema considerará os dados informados pelo usuário nos parâmetros/perguntas da rotina de importação.

**Observação sobre Customização:** Caso o Ponto de Entrada **F430PORT** esteja ativo e retorne `.T.`, o sistema ignora as regras acima e utiliza obrigatoriamente o Banco (EA\_PORTADO), Agência (EA\_AGEDEP) e Conta (EA\_NUMCON) gravados no **Borderô de Pagamento (SEA)**.

Saiba Mais:

[**F430PORT - Define se utiliza o Portador ou o banco de retorno do CNAB na baixa do título**](https://tdn.totvs.com/pages/viewpage.action?pageId=648838953)
