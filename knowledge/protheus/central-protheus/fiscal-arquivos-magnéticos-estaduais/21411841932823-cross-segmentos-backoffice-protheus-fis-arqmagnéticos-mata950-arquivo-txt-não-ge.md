---
article_id: 21411841932823
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: d12da574d384623b55d64ae3e14fa67c1e2498b1e319c5e2ce518ed823b27c96
fetched_at: '2026-06-28T22:42:11.798772+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - MATA950 - Arquivo
  txt não gerado pela rotina
type: support-article
updated_at: '2024-02-19T12:10:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21411841932823-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-MATA950-Arquivo-txt-n%C3%A3o-gerado-pela-rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21411841909015) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O que verificar quando o sistema não gera nenhum arquivo pela rotina **MATA950 - Instruções normativas?**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Verifique como esta preenchida a pergunta "**diretório?**" na *Wizard* da Rotina **MATA950**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21411846730519)

É necessário fechar o caminho escolhido na pergunta **diretório** com uma barra:  
**Exemplo :   
C:\TEMP\**   
  
O sistema separa por filiais a geração dos **arquivos**, ou seja, se você escolher **Seleciona filiais=SIM**, o sistema vai gerar uma pasta dentro do **diretório** escolhido com o nome da **filial** para gerar seu **arquivo**.  
  
**Exemplo :**  
Filial = **01**  
caminho = **C:\temp\**   
sistema gera o arquivo no caminho = **C:\temp\01**
