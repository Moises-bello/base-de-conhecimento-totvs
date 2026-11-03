---
article_id: 360026044891
category: ADVPL - Classe e Função
content_hash: 92b424bf41224e4a14fd6ed25f7b88de2fd1c1bf1ebdb1a715e0fd4bcb66cfa4
fetched_at: '2026-06-28T22:40:15.639635+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Configuração TDS
  11.3 para MAC OS
type: support-article
updated_at: '2022-01-05T13:54:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026044891-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Configura%C3%A7%C3%A3o-TDS-11-3-para-MAC-OS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Em alguns casos com a utilização do sistema MAC OS(Apple) para compilação via TDS 11.3 ou 11.2 tem ocorrido erro na compilação de fontes onde dentro de uma String contem caracteres especiais por exemplo:

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
  
user function tes0023()  
  
alert(OemtoAnsi("Ação de teste ok"))//Neste caso !!  
  
return
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.2 e Protheus 11.80  
  
**Solução**Esse erro ocorre quando caracteres especiais do arquivo editado não estão sendo devidamente convertidos para a codificação correta durante a compilação. Já percebi que nem sempre esse erro ocorre.  
Não existe um padrão do erro, pois já ocorreu tanto em arquivos UFT-8 quanto em Latin1.  
Além das configurações no próprio TDS  em Janelas->Preferências->Espaço de Trabalho .

```
Deixar na janela padrão do arquivo texto como Padrão = CP1252   
  
Janela Novo delimitador da linha do arquivo texto = Padrão Windows 
```

Faça a configuração abaixo como solução.

1. Acesse a pasta da instalação do TDS
2. Clique com o botão direito em "developerStudio.app"(pode ser que esteja sem a extensão dependendo da configuração do seu macOS).
3. Selecione a opção"Mostrar Conteúdo do Pacote".
4. Entre em "Contents", em seguida "macOS".
5. Edite o arquivo "developerStudio.ini" e inclua ao final do arquivo a seguinte linha:

```
-Dfile.encoding=CP1252  
  
-Duser.language=en
```

Observação:  
É importante que caso ocorra esse erro no primeiro acesso do TDS será necessário reinstalar tudo novamente do zero e criar uma nova pasta para o TDS.
