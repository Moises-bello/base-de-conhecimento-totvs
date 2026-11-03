---
article_id: 360020379891
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 30afdd9601fce1ec3bdbda263f1163d205fbe38f41cc83e3f0e093179d366ff4
fetched_at: '2026-06-28T22:41:43.226262+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF -  ATFA070 - Descálculo
  de depreciação
type: support-article
updated_at: '2026-05-04T17:36:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020379891-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA070-Desc%C3%A1lculo-de-deprecia%C3%A7%C3%A3o
---

O descálculo da depreciação no Protheus só pode ser realizado para o último mês calculado, um mês por vez, de forma sequencial para meses anteriores. Após cada estorno, o parâmetro MV\_ULTDEPR é ajustado para o mês anterior. Como alternativa, pode-se restaurar um backup completo para refazer processos a partir de um ponto desejado, porém a manutenção do backup é responsabilidade do cliente.

**Dúvida**  
Quantos descálculo (estornos) podem ser realizados no ativo?  
  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 12  
  
  
**Solução**  
O descálculo da depreciação só pode ser realizado para o último mês calculado.  
  
Por exemplo, se o último mês processado foi **30/04/2026**, somente esse mês poderá ser descálculado diretamente.

Caso seja necessário retornar a meses anteriores (como até fevereiro, por exemplo), será preciso realizar o estorno de forma sequencial, mês a mês.  
  
O sistema permite apenas um estorno por vez. Assim, ao descacular o mês de março, o parâmetro **MV\_ULTDEPR** será ajustado automaticamente para fevereiro, permitindo então o próximo descálculo para janeiro, e assim por diante.  
  
Como alternativa, é possível restaurar um backup completo dos arquivos do módulo de ativos (**SN**) e refazer todas as inclusões, baixas, cálculos e demais processos a partir do ponto desejado.  
  
Importante: a responsabilidade pela manutenção e restauração do backup é do cliente. Após várias execuções de descálculo, não será possível reverter o processo via sistema.  
  
  
**Passos:**

1. Realize o acesso ao sistema com a data-base que deseja realizar o descálculo.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40218074217879)
2. Acesse a rotina em Miscelânea -> Processamentos -> Descálculo mensal.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40218057721623)
3. Na aba "Perguntar", realize o preenchimento dos parâmetros conforme a sua necessidade.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40218074220439)
4. Acesse a aba "Informações", e clique em "Executar"

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40218074221463)

Ao concluir o processo, o sistema estornará a movimentação dos bens calculados e irá retornar o parâmetro MV\_ULTDEPR para o mês anterior.  
  
  
**Saiba mais:**  
[ATFA050/ATFA070: 050UTDEPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006602612-MP-SIGAATF-ATFA050-ATFA070-050UTDEPR?source=search)  
[ATFA050 - Porque o sistema não calcularia a depreciação de um bem?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018327952-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Porque-o-sistema-n%C3%A3o-calcularia-a-deprecia%C3%A7%C3%A3o-de-um-bem)
