---
article_id: 20037851240855
category: REQUISIÇÕES
content_hash: c0fded9e141e5362de1fb53a8477c2eb008c734e30eb53f5483b5618cf188432
fetched_at: '2026-06-28T22:44:37.579319+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - Meu RH - Em qual tabela as justificativas das requisições,
  serão gravadas
type: support-article
updated_at: '2025-11-04T21:11:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20037851240855-RH-Linha-Protheus-Meu-RH-Em-qual-tabela-as-justificativas-das-requisi%C3%A7%C3%B5es-ser%C3%A3o-gravadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20037851173271) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**RH - Linha Protheus - Meu RH - Em qual tabela as justificativas das requisições, serão gravadas  
  
**Ambiente**TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução** **Toda e qualquer requisição vinda do Meu RH**, que tiver um campo de **Justificativa preenchido**, estes dizeres sempre foram gravados na **tabela RDX,**Esta tabela será utilizada apenas **pelo Meu RH e pelo Portal GCH**, para gravar as justificativas das requisições feitas. Sua função será idêntica a da RDY, contudo, será específica do produto Meu RH e do Portal GCH. Com isso, **a tabela RDY deixará de ser utilizada**, sendo esta somente para o **histórico das requisições anteriores.**  
  
Para ter acesso ao pacote de Expedição Contínua do GPE, [clique aqui.](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO_CONTINUA)  
  
Tabela RDX após criada, terá os seguinte campos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20037835009559)  
A RDX terá um compartilhamento totalmente Exclusivo no dicionário de dados.  
  
**IMPORTANTE:  
Quando a montagem da hierarquia de aprovação for por Visões Organizacionais, ou seja, quando o MV\_ORGCFG for igual a 2.**De acordo com a documentação, sobre a **hierarquia de aprovação com o parâmetro MV\_ORGCFG = 2**, algumas tabelas são **compartilhadas entre os Grupos de Empresas, e a RDX também precisará ser.**  
  
Portanto, é **extremamente importante** que, **logo após a execução do UPDDISTR e criação da tabela RDX e sua estrutura, em todos os Grupos de Empresas**, alterar via **Configurador o nome da tabela RDX** dos demais Grupos de Empresas, **centralizando em apenas um Grupo**, assim como já realizado com as demais tabelas quando a estrutura de hierarquia de aprovação é montada, via MV\_ORGCFG = 2.  
  
Exemplo de um ambiente com três Grupos de Empresas e, após executar o UPDDISTR com sucesso em todos eles:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20037851179671)  
  
Neste exemplo, toda a estrutura de hierarquia de aprovação **é centralizada no Grupo de Empresas 01,** com isso, realizar o *login* no **Configurador**, no Grupo de Empresa 01, após, acessar a rotina **Base de Dados > Dicionário > Base de Dados.**  
  
Localizar a tabela RDX e alterar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20037835016599)  
  
O nome abaixo é o que será copiado às tabelas RDX dos demais Grupos de Empresas.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20037851184535)  
  
Neste caso, como a **hierarquia de aprovação via MV\_ORGCFG = 2**, será **centralizada no Grupo de Empresa 01**, **não é necessário alterar** o nome da RDX deste Grupo.  
  
Após, será necessário logar no Grupo de Empresa 02 e no 03 e, acessar a mesma rotina.  
  
Grupo de Empresa 02, tabela criada como RDX020, precisará ser alterada para RDX010:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20037851186327)  
  
**Alterar para RDX010, confirmar e salvar a alteração via Configurador**, no ícone de disquete:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20037835029527)  
  
Confirmar e salvar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20037851193751)  
  
Repetir este mesmo processo para o **Grupo de Empresa 03, alterando de RDX030 para RDX010.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20037851199255)  
  
Lembrando que este processo de alterações da tabela RDX, **será apenas** para quando a hierarquia de aprovação, foi cadastrada mediante **Visão Organizacional, com o parâmetro MV\_ORGCFG = 2.  
  
Para o MV\_ORGCFG = 0 e 1,**as justificativas também serão gravadas na RDX, mas as alterações não precisarão ser efetuadas.  
  
Saiba mais sobre as três maneiras de configurar uma hierarquia de aprovação:  
**[- MV\_ORGCFG = 0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7917580297623)**  
**[- MV\_ORGCFG = 1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043287854)**  
**[- MV\_ORGCFG = 2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051101414)**  
  
Documentações técnicas sobre a nova Tabela RDX:  
<https://tdn.totvs.com/pages/viewpage.action?pageId=808455306>  
<https://tdn.totvs.com/display/NPR/DT+DRHMEURH-12770+Tratamento+para+gravar+dados+na+tabela+RDX>   
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
