---
article_id: 1500002094022
category: RH - Desoneração
content_hash: 755bb1a6fc1c023201e80fe6d551c6a32ef451c7aa91aba70616bda13f348832
fetched_at: '2026-06-28T22:43:42.266798+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o fim da desoneração da folha
  de pagamento
type: support-article
updated_at: '2025-08-04T19:50:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002094022-RH-Linha-Protheus-GPE-Como-parametrizar-o-fim-da-desonera%C3%A7%C3%A3o-da-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33940484517399) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como parametrizar o fim da desoneração da folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**Para que a folha de pagamento deixe de ser calculada com a alíquota reduzida algumas alterações cadastrais deverão ser realizadas:

1. Configure a tabela S037 - Encargos da empresa, coluna 'Rec.Fatur' com o conteúdo igual a 'N' - Não.  
Rotina localizada em: Atualizações >Definição de Cálculos >Manutenção Tabelas.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102963273)  
  
2. Na rotina Mnemônicos, o mnemônico P\_FDESFOL deve ser preenchido com o último Ano e Mês em que a empresa ficou desonerada, ele deve ser preenchido no formato ano e mês: AAAAMM:  
Rotina localizada em: Atualização >Definição de Cálculo >Mnemônicos.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001904702)

**OBS**: Caso tenha cálculo de rescisão no mês da alteração, será necessário efetuar o recalculo após a alteração na tabela S037, para que seja calculado o INSS Empresa sobre as verbas rescisórias.  
  
Para parametrizar as informações a serem enviadas ao **eSocial** utilize a documentação abaixo:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/23319025648535-RH-Linha-Protheus-GPE-Como-parametrizar-o-fim-da-desonera%C3%A7%C3%A3o-da-folha-de-pagamento-para-o-eSocial>

**Saiba mais:**

[RH - Linha Protheus - GPE - Desoneração com o período fechado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047640893-RH-Linha-Protheus-GPE-Desonera%C3%A7%C3%A3o-com-o-per%C3%ADodo-fechado)

[RH - Linha Protheus - GPE - Quais as tabelas envolvidas no fechamento da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017683991-RH-Linha-Protheus-GPE-Quais-as-tabelas-envolvidas-no-fechamento-da-folha)

[Página Centralizadora - Desoneração Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109152-RH-Desonera%C3%A7%C3%A3o)
