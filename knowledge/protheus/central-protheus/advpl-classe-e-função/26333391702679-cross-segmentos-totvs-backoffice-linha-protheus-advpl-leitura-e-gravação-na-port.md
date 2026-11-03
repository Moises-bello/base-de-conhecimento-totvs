---
article_id: 26333391702679
category: ADVPL - Classe e Função
content_hash: 8dca07ab63d7f92945e444734d275c6818093d3d5ac927771d03c19fc388aee0
fetched_at: '2026-06-28T22:40:21.569259+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Leitura e gravação
  na porta serial
type: support-article
updated_at: '2024-09-24T11:13:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26333391702679-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Leitura-e-grava%C3%A7%C3%A3o-na-porta-serial
---

Atualizado em:  
10 de janeiro de 2022 12:24  
*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26333391692823)* Tempo aproximado para leitura: 00:02:00 min

**Dúvida**  
Quais comando existem para o tratamento de comunicação com porta serial?

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80

**Solução**  
Para a utilização de comunicação com porta serial, temos os respectivos comandos :  
  
**MsOpenPort ->** Abre a porta serial para utilização. (As informações para seu uso dependem do periférico)

**MsRead ->**Lê as informações e as coloca no segundo parâmetro da mesma  
**MsWrite ->**Envia as informações necessária para a respectiva porta.  
**MsClosePort ->**Fecha a comunicação com a porta serial utilizada.  
  
Segue abaixo um exemplo para uso conjunto dos respectivos comandos :

```
cTexto := SPACE(50)  
/* A quantidade de espaços variada de acordo com o buffer de dados recebido do periférico  
*/  
  
MsOpenPort(nHandle,"COM1:9600,n,8,1")  
/* Abre a porta serial. Os parâmetros passados entre aspas são (na ordem da direita para a esquerda):  
- Porta Serial  
- Velocidade de transmissão em bps  
- Paridade s/n  
- Quantidade de bits de dados  
- Bits de parada  
Essas informações dependem da configuração do periférico, o padrão esta demonstrado no exemplo acima.  
*/  
  
MsWrite(nHandle,"Comandos a serem enviados")  
/* Envia informações para a porta  
*/  
  
MSRead(nHandle,cTexto)  
/* Lê informações da porta e coloca na variável informada no segundo parâmetro (cTexto no exemplo)  
*/  
  
MsClosePort(nHandle)  
/* Fecha a porta serial  
*/
```

**Saiba mais**  
[Leitura e gravação na porta serial](https://tdn.totvs.com/pages/releaseview.action?pageId=6070761)
