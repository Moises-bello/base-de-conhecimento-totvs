---
article_id: 360024753451
category: RH – DIRF
content_hash: 121c6b3fee2dd3e277961a898568c69c821dcd297c5dba36147a9db77d501314
fetched_at: '2026-06-28T22:44:06.946678+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Criação do campo Relação de Dependência para atender
  leiaute da DIRF
type: support-article
updated_at: '2025-08-19T13:11:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024753451-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-do-campo-Rela%C3%A7%C3%A3o-de-Depend%C3%AAncia-para-atender-leiaute-da-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34286718475543)** Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo Gestão de Pessoal foi criado o campo Relação de Dependência na manutenção de beneficiários para atender leiaute da DIRF nos casos de pensão alimentícia.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Ao importar o arquivo magnético da DIRF para o validador PGD (Programa Gerador da DIRF) era gerado log de ocorrências informando com aviso que a **relação de dependência** não foi informada.

**Solução**Para solucionar essa ocorrência é necessário realizar o **passo a passo** a seguir:  
1. Faça o *backup* do ambiente;  
2. Aplique o pacote de atualização;  
3. Execute o UPDDISTR referente ao dicionários de dados;  
4. Verifique se as datas dos fontes estão realmente atualizados de acordo com o arquivo *contents* no pacote de atualização;  
5. Preencha o campo Relação de Dependência para cada beneficiário pelo caminho **>Atualizações >Funcionários >Beneficiário**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11330836284439)  
  
6. Gere novamente a DIRF através da rotina **Gerar Arquivo** pelo caminho **>Miscelânea >Dirf >Gerar Arquivo;**  
7. Verifique na manutenção de arquivo, em **>Outras ações >Pensão** se o campo foi carregado corretamente:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11330933057047)  
  
8. Gerar o arquivo magnético  
  
  
**Saiba Mais**  
[Pacote atualização expedição contínua](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao_continua)   
[Passo a passo atualizador de dicionário e base de dados - UPDDISTR](http://tdn.totvs.com/pages/viewpage.action?pageId=181965468)  
[RH - Linha Protheus - GPE - Passo a Passo para gerar dados/gerar Arquivo DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012)   
[RH - Linha Protheus - GPE - Passo a Passo para geração do Arquivo magnético da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092)
