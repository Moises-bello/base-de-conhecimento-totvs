---
article_id: 4414505722647
category: Call Center - Telecobrança
content_hash: 7d45fff71161f9595dae72c442eb0a02acc7d32d9f737fd450b601136f580bfc
fetched_at: '2026-06-28T22:41:28.603294+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Lista de cobrança
type: support-article
updated_at: '2024-04-25T12:43:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414505722647-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Lista-de-cobran%C3%A7a
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23049032726807) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar uma lista de cobrança?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

**Premissas**:

* Configuração do parâmetro **MV\_TMKALST**:

1. 1. Avalia primeiramente o perfil do contato;
   2. Avalia primeiramente se o contato possui títulos de acordo com os parâmetros informados;
   3. Avalia somente os contatos inadimplentes. (Recomendado para melhora de performance, pois não irá processar todos os contatos, somente os inadimplentes.).

* Para que as lista gere corretamente, é imprescindível:
  + O cadastro de contato esteja devidamente relacionado ao Cliente;
  + O cadastro do contato (**TMKA070**) esteja devidamente cadastrado informando telefones, endereço e e-mail.

* Configuração do **MV\_TMKLIST**: Determina a não utilização de contatos já presentes em lista de cobrança ativa/em andamento, sendo .F. para um mesmo contato esteja presente em duas listas, que não tenham sido geradas no mesmo dia e .T. não permite o mesmo contato em duas listas, independente do dia de geração.

**Inclusão**:

Procedimento para inclusão da Lista de Cobrança: acesse Atualizações, Cobranças e Lista de Cobrança:

1- Clique em Incluir;

2- Preenchimento dos **Parâmetros.**  Definir o filtro desejado para a seleção dos títulos: prefixo dos títulos, número do título, banco, data de vencimento, data de emissão, natureza e situação;

3- Clique no botão Editar onde permite configurar o perfil dos contatos: nível do contato, ligações pendentes e dias das semana;

4- Informar campos: Nome Lista, Data, Hora (opcional), Tipo Contato (para Lista de Cobrança pode ser contato de voz, cross-posting e mala direta);

5- Salve e escolha se deseja gerar o log Sim ou Não. Para entendimento acesse a aba Log.

Para mais detalhes, acesse: [TMK0078\_Lista\_Cobrança](https://tdn.totvs.com/x/vkNGIQ)
