---
article_id: 360053275594
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 0b027d51e74f0d04a92a756b465f32043ce32b9dde02b3d920ad781e183e71b2
fetched_at: '2026-06-28T22:42:44.444549+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem CONFIGURAÇÃO DE PARÂMETROS
type: support-article
updated_at: '2021-09-14T14:13:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053275594-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-CONFIGURA%C3%87%C3%83O-DE-PAR%C3%82METROS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:03 min**  
**Ocorrência**No módulo **PCP - Planejamento e Controle da Produção**, ao tentar executar o **MATA690 - Carga Máquina** é apresentada a mensagem **CONFIGURAÇÃO DE PARÂMETROS**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Parâmetro **MV\_PROCPCP - Drive e diretório onde serão processados os arquivos binários utilizados na Carga Máquina** não configurado.  
  
**Solução**Para que a mensagem não ocorra é necessário informar um diretório no parâmetro que esteja dentro do **protheus\_data**.  
  
**Exemplo**  
Dentro do **protheus\_data** há a pasta **CARGA**.  
Então no parâmetro **MV\_PROCPCP** deve-se informar **\CARGA\  
  
Importante**Recomendamos também configurar o parâmetro**MV\_DIRPCP - Drive e diretório padrão que o Carga Máquina utiliza para a criação de arquivos de trabalho**com o mesmo diretório do parâmetro**MV\_PROCPCP**
