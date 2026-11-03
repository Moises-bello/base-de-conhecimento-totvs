---
article_id: 360013501352
category: RH - Rescisão
content_hash: 12ae7b972706e085f4823ef8658a27d75f5b0a50e1eadcdc5f09b29c420dace8
fetched_at: '2026-06-28T22:43:48.484020+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Após migração o sistema esta deixando o campo Tipo
  Resc. desabilitado no momento do cálculo
type: support-article
updated_at: '2026-06-25T12:45:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013501352-RH-Linha-Protheus-GPE-Ap%C3%B3s-migra%C3%A7%C3%A3o-o-sistema-esta-deixando-o-campo-Tipo-Resc-desabilitado-no-momento-do-c%C3%A1lculo
---

**Ocorrência**  
Após migração o sistema esta deixando o campo Tipo Resc. desabilitado no momento do cálculo.  
  
**Ambiente**  
TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**  
O problema acontece porque no momento da migração entre a versão 11 e 12, o sistema no campo RG\_PDRESC (SX3 a coluna X3\_FOLDER) cria o arquivo dentro de uma pasta C (só existem as pastas 1, 2 e 3) que não existe na SXA.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Deixe o campo **Tipo Resc.** como editável via **Configurador**, para isso, acesse a rotina **Base de Dados** pelo caminho **>Base de Dados >Dicionários >Base de dados;**  
1.1. Pesquise pela tabela **SRG**;  
1.2 . Altere o campo **Tipo Resc. (RG\_TIPORES)**, deixando a **Propriedade** com **Alterar**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11543191036823)

1.3. **Salve** a alteração em modo **exclusivo** no Sistema:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11543246208535)  
  
2. Entre na tabela XXA e verificar se existe alguma regra de dependência para esse campo - coluna XXA\_CDOM. Em caso positivo, faça um backup e em seguida delete;  
3. Alterar o campo RG\_PDRESC no conteúdo do campo X3\_FOLDER de "C" para "1".

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
