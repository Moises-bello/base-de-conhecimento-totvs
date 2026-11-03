---
article_id: 10621741400087
category: Financeiro
content_hash: 9557e6d772b71227f5708d5482b45846434b34e6ea2657a3b5e7d7165210fdb9
fetched_at: '2026-06-28T22:38:03.412002+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Não foi possível gerar
  os arquivos corretamente Erro ao extrair o Certificado de Autorização no CFGX060  Wizard
  de Conversão de Certificado
type: support-article
updated_at: '2023-11-10T16:51:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10621741400087-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-N%C3%A3o-foi-poss%C3%ADvel-gerar-os-arquivos-corretamente-Erro-ao-extrair-o-Certificado-de-Autoriza%C3%A7%C3%A3o-no-CFGX060-Wizard-de-Convers%C3%A3o-de-Certificado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18972005937431)**Tempo aproximado para leitura: **00:09:00 min**

**Ocorrência**

Ao Acessar o Configurador CFGX060 - Wizard de Conversão de Certificado e selecionar o arquivo .PFX para conversão apresenta a mensagem:

"Não foi possível gerar os arquivos corretamente" Erro ao extrair o Certificado de Autorização no SIGACFG -Wizard de Conversão de Certificado".

**Ambiente**Cross Segmentos - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA710 - Todas as versões

**Causa**

Erro ao Extrair arquivos - CFGX060 - Wizard de Conversão de Certificado

"Não foi possível gerar os arquivos corretamente" Erro ao extrair o Certificado de Autorização

![dica3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10629812057367)

**Solução**

Neste caso, pode verificar a data de validade do certificado, pois o Protheus irá validar a **data de emissão** e **data de vencimento** e a extensão PFX. (O arquivo PFX deve conter o tamanho inicial de 7KB para que tenha comunicação com o Protheus)

**Exemplo**Como verificar a validade do Certificado Digital:  
Acessar o opções da internet > Conteúdo >Certificados >

![unnamed__1_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10629869956247)

Ao clicar no Campo Certificados > Localizar o Certificado na Aba Pessoal > Deve clicar 2x no mesmo e verificar o campo "**Válido a partir de XX/XX/XXX até XX/XX/XXXX**"

![dica4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10629875313687)

O arquivo deve conter a extensão .PFX e seu tamanho inicial de 7KB

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10629968789399)

Após validação acessar o Protheus > **Modulo Configurador> Cadastro> Wizard de Conversão de Certificado.**

Assistente de Conversão de Certificado Digital e seguir as orientações abaixo:

O arquivo .PFX deve estar dentro da pasta system do ambiente Protheus

![unnamed__2_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10629975413655)

Nesse momento o Assistente Conversor irá converter o arquivo .PFX em arquivo extensão .PEM

![unnamed__3_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10630012184343)

**IMPORTANTE:**

Os Caminhos acima devem conter letras **"M****inúsculas"**, conforme exemplo acima, pois podem interferir na conversão dos arquivos

Caso o arquivo conter um tamanho menor do que 7KB, pode seguir as orientações da documentação do saiba mais "**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como Exportar e Aumentar o tamanho do arquivo .PFX ( Certificado Digital - modelo A1 )"** ou pode entrar em contato com o órgão emissor do Certificado (Banco ou Certificadora) para verificar a possibilidade do aumento do tamanho, (Importação das Hierarquias AC no arquivo) devido aos requisitos do Protheus.

**Saiba mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como Exportar e Aumentar o tamanho do arquivo .PFX ( Certificado Digital - modelo A1 )](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10811119314199)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Não foi possível gerar os arquivos corretamente Erro ao extrair o Certificado de Autorização no CFGX060 Wizard de Conversão de Certificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10621741400087)
