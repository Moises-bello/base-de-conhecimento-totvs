---
article_id: 38774771602583
category: eSocial - Gerar XML/ Integração Evento
content_hash: 911a0a620296eb0b29db4c559ecc5eda853f7857ced96b4c1695b82d8c9f3c37
fetched_at: '2026-06-28T22:47:13.133395+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - S-2190 Erro código 8: Grupo #39;Informacoes referentes
  ao registro e a CTPS Digital#39; deve ser preenchido'
type: support-article
updated_at: '2026-03-03T17:45:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38774771602583-RH-RM-FOP-eSocial-S-2190-Erro-c%C3%B3digo-8-Grupo-39-Informacoes-referentes-ao-registro-e-a-CTPS-Digital-39-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38774771565591) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao enviar para o eSocial o evento S-2190 ocorre o erro: Erro código 8: Grupo #39;Informacoes referentes ao registro e a CTPS Digital#39; deve ser preenchido.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões - Todas as versões  
  
  
**Causa**  
O erro ocorre quando não foi preenchido no cadastro Registro Preliminar do funcionário: o tipo de recebimento, a função, salário, e o tipo de contrato. Essas informações são obrigatórias para geração do grupo infoRegCTPS no XML S-2190.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38774745713175)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse no RM Folha de Pagamento: Administração de Pessoal | Registro Preliminar;  
2. Localize e edite o registro preliminar referente a pessoa que ocasionou o erro no evento S-2190;  
3. Faça o preenchimento dos campos sinalizados: Tipo de Recebimento, Salário Mensal, Função e Tipo de Contrato;

**Importante**  
Em 2402/2026, através da Nota Técnica 06/2026, **o item 3.2 entrou em Produção, onde foi alterado a condição de geração do grupo infoRegCTPS** , onde essas informações passaram a ser **obrigatórias** serem preenchidas para aceitação do evento S-2190 no caso de funcionários do tipo Empregado ou Agente Público.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38774745718807)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38774771571479)

Link contendo alteração da NT 06/2026 S-1.3:

<https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-06-2026.pdf>
