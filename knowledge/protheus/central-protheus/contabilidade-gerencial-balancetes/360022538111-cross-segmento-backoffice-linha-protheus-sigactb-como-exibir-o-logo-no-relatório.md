---
article_id: 360022538111
category: Contabilidade Gerencial - Balancetes
content_hash: 32e746bcc84d5e6a270c7394e531c25b1c5074e3aff3cd0f93066d9d237b8ff9
fetched_at: '2026-06-28T22:41:04.187961+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - COMO EXIBIR O LOGO NO
  RELATÓRIO CONTABIL
type: support-article
updated_at: '2022-09-19T19:34:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022538111-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-COMO-EXIBIR-O-LOGO-NO-RELAT%C3%93RIO-CONTABIL
---

**Dúvida**

O logo da empresa foi alterado, mas ao gerar relatórios  é exibido o logo antigo.  
  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus -  Contabilidade Gerencial- Todas as versões **Solução**

1 - A imagem contendo o logo da empresa deve ter 100 pixels de largura por 20 pixels de altura;

2 - A imagem deve ser salva no formato BMP e usando uma paleta de 256 cores;

3 - O nome do arquivo deve iniciar com lgrl, seguido do código da empresa e do código da filial.  
Exemplo: Para a empresa 01 e filial 02 o nome do arquivo deve ser lgrl0102.bmp.  
Para que a mesma imagem seja usada para todas as filiais, basta omitir o código da filial.  
Exemplo: Para todas as filiais da empresa 01 o nome do arquivo deve ser lgrl01.bmp.

Caso a empresa comece a utilizar seu logo nos relatórios ou realize alguma alteração na imagem e ela não apareça ou não seja atualizada ao utilizar o SmartClient HTML, siga os passos abaixo:  
1 - Navegue até o diretório de instalação do SmartClient HTML (Exemplo: C:\PROTHEUS\bin\smartclientHTML);

2 - Dentro do diretório de instalação, navegue até o diretório: server\webapps\ROOT\cache

3 - Exclua todo o conteúdo do diretório cache, independente de serem apenas arquivos ou arquivos e diretórios;

4 - Reinicie o serviço do SmartClient HTML;
