---
article_id: 360015779492
category: Financeiro - Consultas / Relatórios
content_hash: bbedc45fb6fde031300b707f49d057c3c99aeec917b392fbb1ab46f682d9047a
fetched_at: '2026-06-28T22:37:58.512464+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: MP - SIGAFIN - Exibir ou inibir a movimentação bancária no relatório de relação
  de baixas
type: support-article
updated_at: '2021-04-28T15:19:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015779492-MP-SIGAFIN-Exibir-ou-inibir-a-movimenta%C3%A7%C3%A3o-banc%C3%A1ria-no-relat%C3%B3rio-de-rela%C3%A7%C3%A3o-de-baixas
---

**Dúvida**Como exibir ou inibir a movimentação bancária no relatório de relação de baixas (FINR190)?  
   
 **Ambiente**Microsiga Protheus - Financeiro - A partir da versão 12.1.17  
  
**Solução**Para exibir ou inibir a movimentação bancária no relatório Relação de Baixas (FINR190) foi criada uma pergunta no grupo de perguntas **FIN190**, onde pode ser definido se será considerado movimentação bancária no relatório.

Seguir os passos abaixo para atualizar o seu ambiente com a pergunta:

1. Valide se a rotina **FINR190** está com data superior a **07/08/2018**;  
Para validar estando no rotina teclar SHIFT+F6, avançar.  
2. Caso não esteja, efetue *download* do pacote do **[FINR190](https://suporte.totvs.com/portal/p/10098/download?e=704016)**;  
3. Após ter atualizado a rotina será necessário realizar o *download* do **SDFBRA** em anexo;  
4. Coloque o arquivo na pasta **systemload**;  
5. Execute o compatibilizador **UPDDISTR**;  
6. Acesse o menu **Financeiro/Relatórios/Movimento Bancário/Relação de Baixas** e valide se é apresentada a pergunta **Cons. Bx. por mov. bancária?**.  
  
**Saiba Mais**  
Para saber mais informações sobre o conteúdos relacionados acima, acesse o *link* abaixo:  
[Atualizador de dicionário e base de dados - UPDDISTR](http://tdn.totvs.com/pages/viewpage.action?pageId=181965468)

[Fontes de Relatórios](https://suporte.totvs.com/portal/p/10098/download#detail/657324)
