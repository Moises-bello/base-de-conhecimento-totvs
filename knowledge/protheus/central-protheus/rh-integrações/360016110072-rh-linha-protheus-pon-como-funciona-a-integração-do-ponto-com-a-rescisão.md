---
article_id: 360016110072
category: RH - Integrações
content_hash: a2091bd8571b8be68030b0e007ee69720cde7ce04444fb5bb0bf260de35045fa
fetched_at: '2026-06-28T22:44:47.532111+00:00'
product: protheus
section_id: 32419269542935
source: central-protheus
title: RH - Linha Protheus - PON - Como funciona a integração do Ponto com a Rescisão
type: support-article
updated_at: '2026-04-27T12:36:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016110072-RH-Linha-Protheus-PON-Como-funciona-a-integra%C3%A7%C3%A3o-do-Ponto-com-a-Rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29662992771991) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**  
Como funciona a integração do Ponto com a Rescisão?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Antes de realizar a integração deve ser realizado os procedimentos abaixo no modulo do Ponto Eletrônico:  
**1.** Realize toda a leitura e apontamento das marcações do funcionário a ser demitido;  
**2.** Realize o cálculo mensal deste funcionário, com isso, a tabela de resultados (SPB) e/ou Banco de Horas (SPI) serão compostas;  
**3.** Se o funcionário tiver lançamentos de banco de horas, execute o fechamento do banco de horas somente para esta matrícula;  
**4.** Verifique que os resultados serão compostos pelas verbas de desconto e provento do fechamento de banco de horas;  
  
E para que ocorra integração dos Resultados do ponto na **Rescisão**, existem duas opções:  
**1.** Utilizar a rotina padrão de **Integração do Ponto com a Folha de Pagamento**, integrando as verbas calculadas com o roteiro FOL. Desta forma, após a integração, quando for processado o cálculo da rescisão as verbas serão geradas. Passo a aposso de como realizar a integração [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050379453-RH-Linha-Protheus-PON-Integra%C3%A7%C3%A3o-com-a-Folha-de-Pagamento)  
  
**2.** Acessar no **modulo SIGAGPE** na rotina de **calculo de Rescisão** e importar os dados do Ponto através da opção **Importação de Lançamentos de Resultados do Ponto Eletrônico** clicando em Outras Ações e selecionar conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29533649338391)  
  
Após selecionar esta opção, será possível informar o intervalo de datas e se quer Substituir, Desprezar ou Somar as verbas:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29533649343767)**  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
