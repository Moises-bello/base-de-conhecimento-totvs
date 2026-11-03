---
article_id: 360004903712
category: RH - Fechamentos
content_hash: 340eda2b07f3dc58dc07d8fea69cc000ab06c87294a537e33fe9af61c7e09e95
fetched_at: '2026-06-28T22:44:48.927147+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Qual a finalidade das opções Baixar e Limpar o
  Banco de Horas
type: support-article
updated_at: '2026-02-12T12:54:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004903712-RH-Linha-Protheus-PON-Qual-a-finalidade-das-op%C3%A7%C3%B5es-Baixar-e-Limpar-o-Banco-de-Horas
---

**Dúvida**Qual a finalidade das opções **Baixar** e **Limpar** o **Banco de Horas?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**No **[Fechamento do Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013670411-RH-Linha-Protheus-PON-Como-efetuar-o-fechamento-do-banco-de-horas)** **(Miscelânea > Fechamentos > Banco de Horas)**  
Na pergunta **"Lançamentos B.H?"**, estão disponíveis as opções **Baixar** e **Limpar o Banco de Horas**.

- Ao selecionar a opção **Baixar**, o sistema realiza a apuração dos apontamentos de proventos e descontos, efetuando os lançamentos na folha de pagamento conforme as verbas vinculadas aos eventos associados aos IDs de Ponto **023A** e **024A**.  
- O **status** dos apontamentos baixados será atualizado, e a **data da baixa** será registrada automaticamente com base no que foi informado na pergunta '**Data de Pagto Folha?**'

 Veja no destaque da imagem abaixo das perguntas mencionadas para o fechamento do BH:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447885868567)  
  
- Após a execução da rotina de **Fechamento de Banco de Horas** com essa parametrização, os eventos apontados de **16/06/2025 À 23/06/2025**terão a devida **baixa.** Levando em consideração que o **período de apontamento** no **MV\_PONMES** aberto é de **16/06/2025 a 15/07/2025.  
\*\*\*Observe que os apontamentos do mês Junho possuem dados das baixas.** ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447871373079)  
  
- Por sua vez, caso utilizado a opção **Limpar** terá sua funcionalidade de ao executar o fechamento do BH com esta opção serão limpos da tabela SPI, ficando assim os registros na tabela interna demarcados como "deletados" e não sendo possível serem consultados para histórico na tela de manutenção do banco de horas e não serão listados nos relatórios de BH. Deixando assim nenhum registros para histórico e subindo os saldos do período fechado do BH aos resultados de acordo com os eventos respectivos aos saldos do fechamento.  
Antes do fechamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447871379863)  
Após o fechamento do BH com a opção **Limpar:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447885878295)  
**Observação:** Essa opção NÃO permite excluir **apontamentos** já baixados, só serão excluidos os registros que ainda não foram baixados.    
  
  
****Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)**[Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=286212722)  
  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
