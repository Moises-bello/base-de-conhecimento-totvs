---
article_id: 360018428972
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 930beb7133a8018914874a04e79537325c1cb918abdca00a17281d247ccc193f
fetched_at: '2026-06-28T22:40:45.676948+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: ECD_LAYOUT_NÃO_ENCONTRADO.'
type: support-article
updated_at: '2025-04-01T12:26:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018428972-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-LAYOUT-N%C3%83O-ENCONTRADO
---

**Ocorrência**

Ao gerar o ECD é apresentado uma mensagem de ECDLEAYOUT - Leiaute não encontrado.

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
  
**Solução**

Para sanar a ocorrência verifique os passos abaixo:

1- Se os XMLs estão corretamente colocados na pasta "leiaute9" do Protheus conforme indica a documentação

Verifique se os arquivos XML's, foram descompactados na pasta system/Leiaute9

* [Arquivo XML dentro do pacote acumulado ctb](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)
* [Arquivos XML](http://tdn.totvs.com.br/pages/releaseview.action?pageId=235331339)
* baixe o pacote e dentro da pasta config, localize os arquivos XML

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27075987975191)

* Na pasta System crie a p[asta do leiaute , de acordo com o leiuate atual.](https://tdn.totvs.com/pages/releaseview.action?pageId=536725577)
* Exemplo Pasta leiaute9

Importante! Para LINUX é necessário que os arquivos estejam nomeados com letras minúsculas.  
 **![](https://centraldeatendimento.totvs.com/hc/article_attachments/27075987976599)**

2- Esta mensagem também ocorre quando os arquivos ou configuração no INI não estão corretos.

Exemplo de configuração do INI:

RootPath=C:\Protheus\_12\Protheus\_Data\

StartPath=\system

Alterar para :

RootPath=C:\Protheus\_10\Protheus\_Data

StartPath=\system\

 Veja que a barra “\” ao final é essencial para o Protheus encontrar os arquivos XML.

 Importante: Efetuar o Backup antes da atualização.

Saiba mais:

Caso seja ambiente Linux: [MP-SIGACTB:ECD LAYOUT NAO ENCONTRADO, PARA LINUX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022854931-MP-SIGACTB-ECD-LAYOUT-NAO-ENCONTRADO-PARA-LINUX?source=search)

Como atualizar o ECD: [MP - SIGACTB - Como atualizar o ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-MP-SIGACTB-Como-atualizar-o-ECD-)

* [Arquivos XML](http://tdn.totvs.com.br/pages/releaseview.action?pageId=235331339) antigo
