---
article_id: 38990913283223
category: Financeiro - Viagens
content_hash: 733c1826b4dc758dada698bb6fb9483ab7e29a71267f68803db12f645fe24b70
fetched_at: '2026-06-28T22:38:21.275936+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA677 - Lentidão
  no momento de abertura do anexo da prestação de contas
type: support-article
updated_at: '2026-03-19T11:40:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38990913283223-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA677-Lentid%C3%A3o-no-momento-de-abertura-do-anexo-da-presta%C3%A7%C3%A3o-de-contas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38990896608663) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Lentidão no momento de abertura do anexo da prestação de contas.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**  
Foi disponibilizada uma implementação no AppServer que permite selecionar o tamanho do buffer enviado do servidor (AppServer) para o cliente (SmartClient). Para utilizar este recurso, atualize o AppServer para a versão 20.3.2.17 ou superior e realize a configuração do tamanho do pacote.

**Passos**  
Existem duas possibilidades para aplicar essa configuração, dependendo do impacto desejado na aplicação:

Atualize o seu AppServer para a versão 20.3.2.17 ou superior.

Escolha uma das opções de configuração abaixo:

**Opção A: Alteração pontual (Menor impacto geral)**  
Aplicada diretamente na função que está realizando o envio do arquivo. Para isso, utilize a função CpyS2T informando o tamanho desejado em bytes no quinto parâmetro:  
**CpyS2T( [1], [2], [3], [4], [tamanho do buffer enviado em bytes] )**

**Opção B: Alteração genérica (Maior impacto, aplica-se a todos os envios)**  
Aplicada de forma global através do arquivo de configuração do AppServer.  
Acesse o arquivo appserver.ini e adicione as seguintes chaves abaixo da seção [GENERAL]:

[GENERAL]  
**; tamanho do buffer em bytes (Exemplo de valor: 524288)**  
**FileCopyOne=524288**  
**; Opcionalmente, apenas para depuração, ative o log de performance de envio:**  
**FileCopyOneDebug=1**

**Observações Importantes:**

O **tamanho padrão do buffer é de 12 Kb (12288 bytes)**. O novo tamanho configurado deve ser validado, pois o ajuste ideal pode variar de acordo com o cenário da sua rede.

O tamanho do buffer interfere diretamente no consumo: quanto maior o buffer, maior a memória alocada e mais rápida a transferência. Contudo, buffers muito altos podem gerar falhas dependendo das limitações da sua infraestrutura de rede.

Se o seu ambiente for hospedado no TCLOUD, abra um ticket diretamente para a equipe de Cloud solicitando as alterações no arquivo appserver.ini.

Caso a lentidão persista após essas configurações, abra um ticket direcionado à equipe de Tecnologia e Framework para apoio na análise.

**Saiba mais:**

**Download do AppServer:** [**https://suporte.totvs.com/portal/p/10098/download?e=#000006/368/TFAPP/**](https://suporte.totvs.com/portal/p/10098/download?e=#000006/368/TFAPP/)

**Documentação da função CpyS2T:** [**https://tdn.totvs.com/display/tec/CpyS2T**](https://tdn.totvs.com/display/tec/CpyS2T)

**Documentação da chave FileCopyOne:** [**https://tdn.totvs.com/display/tec/FileCopyOne**](https://tdn.totvs.com/display/tec/FileCopyOne)

**Documentação da chave FileCopyOneDebug:** [**https://tdn.totvs.com/display/tec/FileCopyOneDebug**](https://tdn.totvs.com/display/tec/FileCopyOneDebug)
