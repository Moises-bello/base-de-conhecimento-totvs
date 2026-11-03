---
article_id: 360039278214
category: PMS - Projetos
content_hash: 36443f23d7bc7ba7ae7fbb8e7b8436a6b2a772c2640e70dc16bbc5631c23cbe9
fetched_at: '2026-06-28T22:37:14.869206+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - array out of bounds ( 0 of
  35 ) on A203GD1LINOK(PMSA203.PRW)
type: support-article
updated_at: '2024-02-26T18:20:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039278214-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-array-out-of-bounds-0-of-35-on-A203GD1LINOK-PMSA203-PRW
---

**Ocorrência**

Ao alterar a estrutura do projeto é gerado o error.log :

**array out of bounds ( 0 of 35 ) on A203GD1LINOK(PMSA203.PRW) 01/03/2019 15:11:05 line : 1297**

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - todas as versões.  
  
**Causa**

O erro de array out of bounds significa que um campo dentro do array não existe no banco/sx3 ou está com o uso desmarcado ou teve mudança do nível de campo.  
  
Neste caso , pode ser que os campos **AFA\_OPC** e **AFA\_MOPC** que fazem parte do array, possam não estar marcados como usado ou o nível de campo foi mudado do valor padrão.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar o Configurador, base de dados, dicionário de dados, selecionar a tabela AFA e edite;  
2. Deixe os campos **AFA\_OPC** e **AFA\_MOPC** marcados como usado e com o nível igual a 1;  
3. Salve a tabela AFA, atualize o dicionário de dados, reinicie o smartclient e refaça o processo.

**Obs**: Por padrão de sistema, o campo **AFA\_MOPC** não pode ter o nível alterado, ele requerido na validação da getdados pela função **A203GD1LinOk** com o nível 1.

Caso precise efetuar alguma validação de linha junto ao usuário, para digitação diretamente no campo, utilize o ponto de entrada de validação de linha **[A203LINOK1](https://tdn.totvs.com/x/fK9n)**
