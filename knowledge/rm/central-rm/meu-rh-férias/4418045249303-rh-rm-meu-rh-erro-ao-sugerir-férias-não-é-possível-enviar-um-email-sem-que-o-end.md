---
article_id: 4418045249303
category: Meu RH - Férias
content_hash: 4fa95a2d7510a2b4f67646d3aeaa5fe3b8e8b7bd49136044eea091dbbf3534b1
fetched_at: '2026-06-28T22:47:31.677059+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: RH - RM - Meu RH - Erro ao sugerir Férias, não é possível enviar um email sem
  que o endereço seja informado
type: support-article
updated_at: '2026-06-19T12:05:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418045249303-RH-RM-Meu-RH-Erro-ao-sugerir-F%C3%A9rias-n%C3%A3o-%C3%A9-poss%C3%ADvel-enviar-um-email-sem-que-o-endere%C3%A7o-seja-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22160826827927) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao realizar uma sugestão de férias pelo Meu RH, é apresentado a seguinte mensagem de erro: "Não é possível enviar um e-mail sem que o endereço do destinatário seja informado."  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Esse incidente ocorre, quando está habilitado o envio de férias nas sugestões de férias, porém o sistema não localiza um endereço de e-mail válido para o responsável pela aprovação (Chefe, Supervisor ou gestor definido pela Hierarquia por Posição).  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27419095890455)**  
Caminho do parâmetro: *Folha de Pagamento / Configurações / Parametrizador / RM Portal / Edite o quiosque vinculado ao funcionário / E-mail de férias > 'Enviar Email na sugestão e aprovação de férias'.*  
  
**Solução**  
Selecione a opção da estrutura hierárquica que é utilizada em seu ambiente:

#### **🔹**[**Chefe/Supervisor**](#chefe)

#### **🔹**[**Hierarquia por Posição**](#hierarquia)

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

### Chefe/Supervisor

Para facilitar, elaboramos uma consulta SQL que retornam todos os Chefes, Supervisores e Externos sem e-mail preenchido, para que seja possível um ajuste geral da base. Execute ela através do SGBD ou pelo Menu [Visões de dados do RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13055235652759-Cross-Segmentos-Backoffice-RM-BI-Funcionalidades-de-consultas-SQL-menu-Vis%C3%B5es-de-Dados) para realizar o levantamento:

```
SELECT DISTINCT *
FROM (
    SELECT 'CHEFE' AS TIPO, PF.CHAPA, PF.NOME, PP.EMAIL,
           PSC.CODSECAO, PSC.CODCOLIGADA
    FROM PSUBSTCHEFE PSC
    JOIN PFUNC PF ON PSC.CODCOLSUBST = PF.CODCOLIGADA
                 AND PSC.CHAPASUBST = PF.CHAPA
    JOIN PPESSOA PP ON PP.CODIGO = PF.CODPESSOA

    UNION ALL

    SELECT 'SUPERVISOR', PF.CHAPA, PF.NOME, PP.EMAIL,
           PSS.CODSECAO, PSS.CODCOLIGADA
    FROM PSUBSTSUP PSS
    JOIN PFUNC PF ON PSS.CODCOLIGADA = PF.CODCOLIGADA
                 AND PSS.CHAPASUBST = PF.CHAPA
    JOIN PPESSOA PP ON PP.CODIGO = PF.CODPESSOA

    UNION ALL

    SELECT 'CHEFE EXTERNO', PE.CODEXTERNO, PP.NOME, PP.EMAIL,
           PCE.CODSECAO, PCE.CODCOLIGADA
    FROM PEXTERNO PE
    JOIN PCHEFEEXTERNO PCE ON PE.CODEXTERNO = PCE.CODEXTERNO
    JOIN PPESSOA PP ON PP.CODIGO = PE.CODPESSOA

    UNION ALL

    SELECT 'SUPERVISOR EXTERNO', PE.CODEXTERNO, PP.NOME, PP.EMAIL,
           PSE.CODSECAO, PSE.CODCOLIGADA
    FROM PEXTERNO PE
    JOIN PSUPERVEXTERNO PSE ON PE.CODEXTERNO = PSE.CODEXTERNO
    JOIN PPESSOA PP ON PP.CODIGO = PE.CODPESSOA
) X
WHERE EMAIL IS NULL;
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41345951001495)

Após o resultado da consulta, acesse o cadastro dos funcionários retornados no RM e preencha um e-mail válido no campo **'E-mail'** da aba **Identificação**.

#### Validação pontual

Caso deseje identificar especificamente quem é o responsável pela aprovação de determinado colaborador, siga os passos abaixo:

1. Acesse no RM o cadastro de funcionários e verifique em qual seção está lotado o colaborador que recebeu o erro ao sugerir as férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27419116862743)  
  
2. Acesse na **folha de pagamento** > **Administração de Pessoal** → **Chefes e Supervisores**. Localize a seção identificada no passo anterior e verifique quem está cadastrado como Chefe ou Supervisor.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27419116866199)  
  
**Observação:**Caso a seção não possua Chefe ou Supervisor cadastrado, o sistema buscará automaticamente o responsável da **seção pai**. Exemplo: Se a seção **01.03** não possuir chefe cadastrado, o sistema enviará o e-mail para o Chefe da seção superior (**Filial 01**).  
  
3. Acesse o cadastro de funcionário do chefe ou supervisor identificado e valide se o e-mail está preenchido corretamente no cadastro de funcionário e usuário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27419095888791)  
  
Após preencher o e-mail do responsável, solicite que o colaborador realize uma nova sugestão de férias.

## Hierarquia por Posição

Para um ajuste geral, execute a consulta abaixo para localizar todos colaboradores vinculados à estrutura de hierarquia que estão sem e-mail preenchido:

```
SELECT DISTINCT
       PF.CODCOLIGADA,
 PF.CHAPA,
 PF.NOME,
       PS.EMAIL AS EMAIL_FUNCIONARIO,
       GU.EMAIL AS EMAIL_USUARIO
FROM VPOSICAO VP
INNER JOIN PFUNC PF
 ON PF.CHAPA = VP.CHAPAFUNCIONARIO
INNER JOIN PPESSOA PS
 ON PS.CODIGO = PF.CODPESSOA
INNER JOIN GUSUARIO GU
 ON PS.CODUSUARIO = GU.CODUSUARIO
INNER JOIN VHIERARQUIAPOSICAO VHP
 ON VHP.CODPOSICAO = VP.IDPOSICAO
WHERE PS.EMAIL IS NULL OR GU.EMAIL IS NULL
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41345951002903)

Após o resultado da consulta, acesse o cadastro dos funcionários retornados no RM e preencha um e-mail válido no campo **'E-mail'** da aba **Identificação**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41345951004439)

Se todos os e-mails estiverem preenchidos e o erro persistir, verifique se as hierarquias superiores possuem posições vinculadas. Exemplo de estrutura hierárquica:

* **[1]** **Presidente** *(Hierarquia Pai)* → posição vinculada ao colaborador Gilmar
* **[1.2]** **Vice-Presidência** *(Hierarquia superior Presidente)* → sem posição vinculada
* **[1.2.3]** **Gestão** *(Hierarquia superior Vice)* → posição vinculada à colaboradora Zélia

Nesse cenário, quando Zélia solicitar férias, ocorrerá o erro, pois a hierarquia superior à sua (**Vice-Presidência**) não possui nenhuma posição associada.

Para está validação, sugerimos utilizar a visão do [Organograma](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047908833-RH-RM-RHU-Organograma) selecionando a visão de Hierarquia. Expanda até o nível da hierarquia do colaborador e valide se hierarquia superior apresenta a descrição **"Não possui posição associada."**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41345965597207)  
  
Para vincular uma posição à uma hierarquia, há duas formas: através do anexo da posição ou através do assistente **Manutenção de Hierarquia/Posição.** Confira a documentação com os passos detalhados:  
[RH - RM - RHU - Hierarquia por Posição: Vincular a posição à hierarquia](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6572321447575-RH-RM-RHU-Hierarquia-por-Posi%C3%A7%C3%A3o-Vincular-a-posi%C3%A7%C3%A3o-%C3%A0-hierarquia)

Após preencher os e-mails corretamente e certificar que todas hierarquias superiores possuem posição associada, será possível realizar a solicitação de férias com o envio de e-mail habilitado.

**Importante**  
Após realizar as validações descritas neste artigo, execute também a rotina de Manutenção do Cadastro de Seções  através do menu executar em todas as coligadas da base. Esse procedimento atualiza a coluna **PSECAO.CODIGOPAI** e corrige possíveis inconsistências na estrutura hierárquica das seções.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41345965597463)
