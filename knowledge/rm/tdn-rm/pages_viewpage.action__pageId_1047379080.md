---
content_hash: bd99f9f08ada9a29e8c908e2bdde908841b77c3e3817d5908b7889669c67b79c
fetched_at: '2026-06-29T00:05:51.137169+00:00'
page_id: '1047379080'
product: rm
source: tdn-rm
title: Publicação de Banner's Informativos no Portal de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1047379080
version: 4
---

## 1. Objetivo

Definir o procedimento para disponibilização de banners informativos no **Portal de Imóveis**, bem como descrever as propriedades obrigatórias para sua correta exibição e funcionamento.

Foi implementado no **Portal de Imóveis** um mecanismo genérico para publicação de banners informativos (novidades, comunicados e integrações), sem a necessidade de instalação de patch ou atualizaçãoInformativos Portal  de versão.

A funcionalidade utiliza a engine do **TOTVS News** para gerenciar e disponibilizar os banner's no portal.

---

## 2. Funcionamento

Para que um banner seja exibido no Portal de Imóveis, é necessário:

1. Disponibilizar a imagem no diretório correspondente do Google Drive.
2. Configurar um arquivo JSON contendo os metadados do banner.
3. Publicar o JSON conforme padrão utilizado pelo TOTVS News.

Cada item informado no JSON gerará automaticamente um modal no portal.

É possível cadastrar quantos informativos forem necessários — será exibido um modal para cada objeto ativo presente no arquivo.

**O acesso ao diretório do Google driver é restrito, ficou acordado que a responsabilidade de atualizar as informações das publicações será do PO/UX**

* Diretório do driver para atualizar imagem e atualizar arquivo Json   
  <https://drive.google.com/drive/folders/1SmxpyYWWb_liMweATnSG2eVN0dkKbadq>
* Caminho fixo do Json de imagens do Porta de imóveis  
  <https://totvsnewsrmstorage.totvs.com/totvs-news-static-data/assets/CP/InformativosPI.json>

## Observações

O Portal de Imóveis valida a existência dos arquivos obrigatórios, tanto a **imagem do banner** quanto o **arquivo JSON**. Caso algum deles não seja encontrado, o banner não será exibido.

A exibição do banner considera obrigatoriamente os seguintes campos:

* + **`ativo`**: determina se o banner está habilitado para exibição.
  + **`data_expiracao`**: define a data limite em que o banner permanecerá visível. Após essa data, o banner não será mais apresentado.
  + **`guid`**: identificador único do informativo.

    - Esse identificador é utilizado para registrar quando o usuário optar por não visualizar novamente o informativo.
  + **`name_banner`**: nome do arquivo da imagem do banner, previamente disponibilizado no Google Drive.
  + A propriedade **`title`** será utilizada como texto de cabeçalho do banner.
  + Caso a propriedade **`actionHotsite`** esteja preenchida, ao clicar no banner:

    - O usuário será redirecionado para a página configurada.
    - Será realizado o registro da ação no *licence.*

---

## 3. Estrutura do JSON

A estrutura do arquivo deve seguir o padrão abaixo:

{  
     "informativos": [  
          {  
             "guid": "112DD94E-40F9-40CA-8F5A-0D2E6BBBE978",  
             "ativo": true,  
             "codSistema": "Imb",  
             "data\_expiracao": "2026-03-15",  
             "name\_banner": "OQDigital\_BannerTCGI.jpg",  
             "actionHotsite": "ImbActionOQDigitalPI",  
             "title": "Integração OQ Digital",  
             "url\_redirect": "<https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-indicacoes-imobiliarias-by-oq-digital/>"  
          }  
     ]  
}

---

## 4. Descrição dos Campos

| Campo | Descrição |
| --- | --- |
| **guid** | Identificador único do informativo (recomenda-se UUID). |
| **ativo** | Define se o banner será exibido (`true` ou `false`). |
| **codSistema** | Código do sistema ao qual o informativo se aplica (ex.: `Imb`). |
| **data\_expiracao** | Data limite para exibição do banner (formato `YYYY-MM-DD`). |
| **name\_banner** | Nome do arquivo da imagem disponibilizada no Google Drive. |
| **actionHotsite** | Identificador interno da ação vinculada ao banner. |
| **title** | Título exibido no modal. |
| **url\_redirect** | URL para redirecionamento ao clicar no banner. |

```

```
