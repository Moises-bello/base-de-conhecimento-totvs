---
article_id: 30309557392919
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 0a15b9ef9ef3bee66c3d2aac57c3d0e050687839cc24a1f086177b463478ab55
fetched_at: '2026-06-28T22:37:55.142576+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Aumentar
  o tamanho do campo da informação de arquivos
type: support-article
updated_at: '2025-02-28T14:20:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30309557392919-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-CNAB-Aumentar-o-tamanho-do-campo-da-informa%C3%A7%C3%A3o-de-arquivos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30309581161367) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Como aumentar o tamanho do campo da informação de arquivos de configuração e de envio / retorno nos parâmetros das rotinas de CNAB

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Hoje o Protheus possui a limitação de arquivos para o CNAB de 99 caracteres, depende do tipo de processo utilizado no grupo de perguntas, ou seja, o tamanho da pasta até o arquivo.extensão pode conter até 99 caracteres, exemplo de limite por tipo.

Tipo **Edit**: Limite de 50 caracteres, exemplo:  
**C:\TOTVS\baseline\237\_29670\_2430\_03012025001.ret**  
  
Tipo **File**: Limite de 99 caracteres, exemplo:  
**C:\TOTVS\baseline\cnab\modelo1\retorno\237\contasrecebimento\3456708\237\_29670\_2430\_03012025001.RET**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30309581162135)**

Para alterar, recomendamos deixar a caixa da pergunta como buscar arquivo, assim como mostra a imagem, arq. Configuração e arq. de saída/entrada, dentro do Configurador, **Caminho: Base de dados>dicionario>base de dados>Perguntas.**

No CNAB é possível alterar os grupos de perguntas abaixo:  
  
FIN650 - Relatório de Retorno CNAB  
AFI430 - Retorno de Pagamentos  
AFI420 - Arquivo de Pagamentos   
AFI150 - Arquivo de Cobranças  
AFI200 - Retorno de Cobranças  
FIN680 - Extratos Febraban  
AFI151 - Instrução de Cobranças  
  
**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações e dúvidas para uso do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Principais-configura%C3%A7%C3%B5es-e-d%C3%BAvidas-para-uso-do-CNAB)
