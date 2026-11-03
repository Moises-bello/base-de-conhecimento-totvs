---
article_id: 25997248589591
category: eSocial - Gerar XML/ Integração Evento
content_hash: 607d59c08ab4630aac197ec161edf16b25a4d3f92cba132863cb2206e1d8d1ca
fetched_at: '2026-06-28T22:47:11.956378+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao gerar o XML S-2300 ocorre erro na validação do
  campo ''cnpjInstEnsino'': CNPJ Inválido!'
type: support-article
updated_at: '2026-03-12T00:08:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25997248589591-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-2300-ocorre-erro-na-valida%C3%A7%C3%A3o-do-campo-cnpjInstEnsino-CNPJ-Inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25997248526359) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao gerar o XML S-2300 ocorre **Erro na validação do campo 'cnpjInstEnsino': CNPJ Inválido!**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25997248531351)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial- Todas as versões  
  
**Causa**  
Para o eSocial, o CNPJ só deverá ser gerado quando a instituição for do Brasil e deve possuir 14 algarismos, não sendo considerados caracteres especiais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25997234868759)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse Folha de Pagamento | Administração de Pessoal | Edite o cadastro do Estagiário;  
2. Em Dados do Estágio edite a Instituição de Ensino do Estágio e identifique se o CNPJ consta corretamente preenchido e exclua os caracteres especiais;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25997248546199)

3. Realize a correção e após regere o XML.
