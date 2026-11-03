---
article_id: 5697877326231
category: eSocial - Tabelas/Não Periódicos
content_hash: e871d087c52f1c7b549f2c67cdce0d7b8580cc5027775149ce630eda0037b9db
fetched_at: '2026-06-28T22:47:10.199388+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial  - Como gerar o evento S-1005 quando existe mais de
  um CAEPF cadastrado para o mesmo CPF
type: support-article
updated_at: '2026-02-02T15:06:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5697877326231-RH-RM-FOP-eSocial-Como-gerar-o-evento-S-1005-quando-existe-mais-de-um-CAEPF-cadastrado-para-o-mesmo-CPF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38101829822359) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como gerar *tag* tpInsc no evento S-1005 quando existe mais de um CAEPF cadastrado para o mesmo CPF?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Para a parametrização necessária, realize os seguintes passos:  
1. Acesse o menu **RH | Folha de Pagamento | Configurações | eSocial | Configurações Gerais | Configurações Gerais 2/7** e marque o parâmetro **Utiliza quebra de CAEPF** e configure a máscara de quebra que será considerada para a geração do estabelecimento. Deverá ser a mesma do **Código de quebra para CNPJ**.

![para.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5697905852183)

2. Após realizar a configuração do item acima, será permitido cadastrar seções (nível de quebra de CNPJ/CPF) informando o mesmo CPF porém com CAEPF diferente. Acesse **Cadastros | Seções.**

![se__o.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5698048887319)

![se_a.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5698084567703)  
3. Na geração do xml do evento S-1005 serão gerados dois estabelecimentos, sendo um para cada CAEFP. Acesse **eSocial | Geração do XML Eventos de Tabela/Não Periódicos.**

**![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5698191319831)**

**![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5698192653079)**

**Observação**  
Na geração do xml do evento S-1200 será informado o CAEPF conforme alocação do funcionário.

![22222.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5698514186775)

**Saiba mais**  
Para mais informações acesse [CAEPF](https://totvssuporte.zendesk.com/knowledge/articles/360031814193/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F360031814193).
