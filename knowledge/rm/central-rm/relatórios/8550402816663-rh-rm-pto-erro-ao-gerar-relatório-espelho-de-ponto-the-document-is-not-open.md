---
article_id: 8550402816663
category: Relatórios
content_hash: 5ad063fa9e204117ba3f76b7c5d4b74a08871b20d206ba423627273dc04ca7e0
fetched_at: '2026-06-28T22:46:39.259032+00:00'
product: rm
section_id: 1500000861642
source: central-rm
title: 'RH - RM - PTO - Erro ao gerar relatório espelho de ponto: The document is
  not open'
type: support-article
updated_at: '2025-02-19T15:39:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8550402816663-RH-RM-PTO-Erro-ao-gerar-relat%C3%B3rio-espelho-de-ponto-The-document-is-not-open
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981943674135) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**

Ao executar relatórios no RM, é apresentado o erro:

*The document is not open.  
O documento não está aberto.*

![erro1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8550364729367)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Causa**Esse incidente ocorre, pois, a parametrização do sistema está incorreta para tag FlieServerPath e LogPath ou inconsistência no leitor de PDF da máquina.   
  
**Solução**

Para solucionar a inconsistência, siga as orientações abaixo:

1. Configure as TAG *FileServerPath* e *LogPath*em seus servidores de App e JOB (TODOS), apontando para uma unica pasta compartilhada na rede, conforme documento [Configurando FileServerPath e LogPath](http://tdn.totvs.com/display/LRM/Configuracao+das+Tags+FileServerPath+e+LogPath).  
     
   **Importante**O caminho da pasta configurado dentro das TAGs deve ser o caminho do compartilhamento.  
   Exemplo: \NomeServidor\NomePasta  
   As permissões na pasta compartilhada devem ser para todos (everyone), caso haja restrição em sua rede, aplique as permissões pelo menos para o usuário que está inicializando o serviço do host, por exemplo: Administrador de Rede:    
   ![CP1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8550400558487)
2. Tente gerar o relatório em PDF.   
   Em alguns relatórios, como por exemplo, gerar Espelho do Cartão, recomenda-se gerar relatório em PDF, conforme print abaixo, quando o volume de dados é muito grande e o Reports não suporta:   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30090567166359)
3. Reinstalar o leitor de PDF e realizar novo teste.
