---
content_hash: 3d8b2270f93ed52342d29819cdb4269399015676aea4a30f1cf21ed25734c497
fetched_at: '2026-06-29T00:11:21.358644+00:00'
page_id: '694102178'
product: rm
source: tdn-rm
title: FAQ - Ocorrências Comuns
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=694102178
version: 5
---

**Objetivo:**

---

       O objetivo deste documento é apresentar as principais dúvidas e ocorrências do eSocial mapeadas pela equipe de atendimento técnico.

---

## **LEIAUTE S-1.0**

### VERSÃO DE LEIAUTE

**DÚVIDA**

- Qual o período de convivência e o que fazer após seu término?

**SOLUÇÃO**

O período de convivência, durante o qual são recebidos eventos do eSocial nas versões 2.5 e S-1.0, se encerrou dia 22/05/2022. A partir de **23/05/2022**, apenas eventos enviados na versão S-1.0 serão recebidos pelo eSocial.

Veja mais informações em:

[RM eSocial - Período de convivência das versões de leiaute](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5574246669207)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**DÚVIDA**

- Preciso atualizar minha versão para utilizar o leiaute S-1.0?

**SOLUÇÃO**

A sugestão da TOTVS é que o ambiente esteja sempre atualizado com o Patch mais atual do Release, para que correção de não conformidade estejam aplicadas no ambiente. Contudo, O leiaute S-1.0 NT 03/2021 já está no mercado desde os Patches 12.1.32.244, 12.1.33.183 e 12.1.34.102, e o leiaute S-1.0 NT 04/2021 já está no mercado desde os Patches 12.1.32.244, 12.1.33.183 e 12.1.34.102. Ou seja, caso esteja em versão igual ou superior às citadas, já será possível utilizar o leiaute S-1.0 no RM.

[RM eSocial - Simplificação eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003462802)

Para versões do TAF, favor acessar o documento abaixo:

[Automação Fiscal - Como atualizar a versão do layout para o e-Social Simplificado S 1.0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022224812)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### ERROS DE INTEGRAÇÃO

**OCORRÊNCIA**

- Erro ao transmitir eventos ao Governo:**"Código do erro: 000"**

**-** Erro ao transmitir eventos ao Governo: **"403****- Leiaute do evento inválido"**

**SOLUÇÃO**

Alterar os leiautes do RM e TAF, gerar novamente os XMLs no RM e realizar uma nova transmissão para TAF/Governo

[RM eSocial - Alteração da versão do leiaute do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5574246669207)

[Automação Fiscal - Como atualizar a versão do layout para o e-Social Simplificado S 1.0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022224812)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**OCORRÊNCIA**

- Cliente Middleware - Erro ao transmitir eventos ao Governo:**"O evento ID xxxxx foi rejeitado pelo RET", sem código de erro**

**SOLUÇÃO**

Alterar o leiaute do eSocial no RM, gerar novamente o XML no RM e realizar uma nova integração com o Governo

[RM eSocial - Alteração da versão do leiaute do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5574246669207)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**OCORRÊNCIA**

- Erro ao transmitir eventos S-2200/S-2206 ao Governo: **"Código do erro 553 - Grupo #39;FGTS#39; não deve ser preenchido."**

**SOLUÇÃO**

Alterar os leiautes do RM e TAF, gerar novamente os XMLs no RM e realizar uma nova transmissão para TAF

[RM eSocial - Alteração da versão do leiaute do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5574246669207)  
[Automação Fiscal - Como atualizar a versão do layout para o e-Social Simplificado S 1.0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022224812)

Após integrar o evento com o TAF, acessar o registro do funcionário e validar se a informação de FGTS está preenchida no cadastro. Caso afirmativo, excluir a informação e tentar integrar novamente o evento com o governo.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**OCORRÊNCIA**

- Erro ao transmitir eventos S-2300 ao Governo: **"O campo 'matrícula' do registro 'infoTSVInicio' é obrigatório e não está preenchido"**

**SOLUÇÃO**

Ao cadastrar um funcionário sem vínculo com o leiaute 2.5 configurado no sistema, a matrícula eSocial não é preenchida por não ser obrigatória neste leiaute. Contudo, com a obrigatoriedade do S-1.0, a matrícula passa a ser obrigatória no XML para todos os funcionários. O sistema, porém, não permite o preenchimento da matrícula para o funcionário cadastrado antes da utilização do leiaute S-1.0, sendo necessário então excluir o cadastro do funcionário do sistema e cadastrá-lo novamente, ou realizar a inserção da matrícula via banco de dados (script de inserção não faz parte do escopo do suporte).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### GERAÇÃO DE XML

**OCORRÊNCIA**

- Erro ao transmitir eventos S-2200/S-2206 ao Governo: **"Erro na validação do campo 'tpJornada': Valores válidos: 2,3,4,5,6,7,9."**

**SOLUÇÃO**

O erro ocorre pois no leiaute S-1.0 foram excluídos alguns tipos de jornada, que eram válidos no leiaute 2.5. Assim, o erro é apresentado quando o campo Tipo de jornada eSocial não está com os valores válidos previsto no leiaute S-1.0, sendo os válidos: 2,3,4,5,6,7,9. Para ajuste, seguir o artigo abaixo:

[RM eSocial - Erro na validação do campo 'tpJornada': Valores válidos: 2,3,4,5,6,7,9](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6150968736663)

---

## **RUBRICAS**

**OCORRÊNCIA**

- Erro ao transmitir eventos S-1010 ao Governo: **"Erro 244 ao enviar S-1010: Natureza da rubrica inválida"**

**SOLUÇÃO**

O erro ocorre quando a natureza de rubrica utilizada está incorreta ou expirada. Veja a documentação abaixo as orientações para ajuste:

[RM eSocial - Erro 244 ao enviar S-1010: Natureza da rubrica inválida](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403022584727)

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**DÚVIDAS**

- Qual natureza de Rubrica utilizar nos eventos e onde informá-las?

**SOLUÇÃO**

A natureza de rubrica é informada dentro do módulo Folha de Pagamento, menu Administração de Pessoal | Eventos, campo Natureza da Rubrica (eSocial).   
A TOTVS não orienta qual natureza de rubrica deve ser informada nas verbas, ficando tal escolha a cargo da própria empresa. O que podemos orientar é que a natureza esteja condizente com o Anexo I do Layout eSocial utilizado.

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**
