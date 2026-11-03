---
article_id: 360056070293
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 6abadaf786bc74e44be0217b7fd13e5afcf0f9145989ef8a307f838baca9f15f
fetched_at: '2026-06-28T22:39:56.368741+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Código do
  Município não homologado, para municípios homologados
type: support-article
updated_at: '2025-06-02T12:22:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056070293-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-C%C3%B3digo-do-Munic%C3%ADpio-n%C3%A3o-homologado-para-munic%C3%ADpios-homologados
---

**Ocorrência**Ao acessar a rotina FISA022 é apresentado a mensagem: **"Código de município XXXXXXX não homologado na versão do TSS"**.Exemplo (prefeitura Uruguaiana/RS):

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091707094/mceclip3.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Essa mensagem ocorre por dois motivos:  
  
1. De fato o município não está homologado no TSS, o qual poderá ser verificado se consta na relação abaixo:  
- [Municípios Homologados TSS (NFSE)](https://tdn.totvs.com/pages/releaseview.action?pageId=4814340)  
2. O município está homologado, porém o Protheus ou TSS está guardando alguma informação incorreta em uma variável global;  
3. O código do município não está no padrão IBGE (7 dígitos) - Consulta: [clique aqui.](https://cidades.ibge.gov.br/brasil/panorama)  
  
**Solução**Para a segunda opção, será necessário que seja zerada essa variável para correção do problema, através dos seguintes procedimentos:  
  
1. Acesse o Configurador (SIGACFG), faça uma cópia da URL atual e altere a URL do parâmetro MV\_SPEDURL para uma aleatória, exemplo: [localhost.teste:999;](http://localhost:12001/)  
2. Acesse a rotina e aguarde, onde irá apresentar uma falha de comunicação com o TSS;  
3. Após isso feche a rotina, altere o parâmetro MV\_SPEDURL novamente para a URL correta do TSS;  
4. Acesse a pasta PROFILE do Protheus e delete os arquivos com nome FISA022 e FIS022 com extensão .PRB;  
5. Feito isso **deverá reiniciar o Appserver** **do Protheus por completo,** após isso acesse a rotina novamente.
