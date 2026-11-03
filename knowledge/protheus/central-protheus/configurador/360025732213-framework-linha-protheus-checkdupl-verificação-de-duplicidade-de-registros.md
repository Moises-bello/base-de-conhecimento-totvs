---
article_id: 360025732213
category: Configurador
content_hash: 0b215dc82d7f5e3b198ba9f0ba23b533ae7ccfd91f3e5349f89ff88fd6e6a11b
fetched_at: '2026-06-28T22:42:18.932943+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: 'Framework - Linha Protheus  - CheckDupl: Verificação de Duplicidade de Registros'
type: support-article
updated_at: '2024-05-08T11:36:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025732213-Framework-Linha-Protheus-CheckDupl-Verifica%C3%A7%C3%A3o-de-Duplicidade-de-Registros
---

**Dúvida**  
Existe alguma rotina para checar a duplicidade de registros antes de efetuar uma migração?  
  
**Ambiente**  
Protheus - Configurador - A partir da versão 11  
  
**Solução**  
Sim, a rotina **CheckDupl**, que pode ser adicionada ao Configurador, permite efetuar a verificação de duplicidade de registros na base antes de efetuar alguma migração.  
  
Primeiramente, é necessário baixar o pacote do **CheckDupl** no Portal do Cliente.  
1. Acesse o Portal do Cliente: <http://suporte.totvs.com>2. Clique em **Downloads**3. Linha **Protheus**  
4. Faça uma busca por **CHECKUNIQUE**  
5. Baixe o arquivo referente a sua **versão** e **base**  
6. Após baixar o patch, aplique-o no seu **ambiente**.  
7.Tendo aplicado o patch, é necessário criar um item de menu que chame essa rotina. Para isso, acesse o Configurador > Ambiente > Cadastros > Menus, edite o menu do Configurador, incluindo um novo item com as especificações abaixo:  
Descrição: Verificar Duplicidade  
Programa: CheckDupl  
Status: Habilitado  
Módulo: Configurador  
Tipo: Função Protheus  
  
8. Clique em **Ok**9. Clique em **Gerar**e digite **SIGACFG**para que a alteração seja salva no menu existente  
10 . Clique novamente em gerar e confirme a inclusão do menu  
  
Procedimento para utilização  
1. No Configurador execute a opção **Verificar Duplicidade**. O Sistema apresenta a janela de apresentação do Wizard.  
2. Clique em **Avançar**  
3. Na tela seguinte, informe onde se encontra o arquivo **SX2.UNQ**. Todas as tabelas cadastradas no **SX2** serão carregadas.  
4. Selecione as tabelas que deseja verificar a **duplicidade de registros**.  
5. Clique em **Finalizar** e confirme a mensagem de busca por duplicidade. Este processo pode demorar, aguarde.  
6. Após o término da verificação, o Sistema mostra uma tela com todas as duplicidades encontradas.  
7. Selecione os registros que deverão ser **removidos** da tabela.  
  
\*Para cada chave duplicada, deve-se deixar apenas uma ocorrência, para que na base, fique sempre um registro válido.  
  
\*\*Os registros selecionados são removidos da tabela original e copiados para uma tabela com o mesmo nome, como o sufixo \_UNQ. Por exemplo: SA1010\_UNQ.  
  
\*\*\*A opção Marcar registros pode ser usada para que o Sistema sugira os registros a serem excluídos da base. Porém, nem sempre os critérios adotados pelo Sistema são os mais apropriados para a base em questão. Desta forma, antes de remover os registros, é importante que seja feita uma análise completa dos dados.  
  
8. Quando todos os registros duplicados, de uma mesma tabela, estiverem selecionados, clique em **Eliminar Duplicidades** para que eles sejam removidos.  
9. Algumas opções disponíveis podem ser executadas:  
  
**Visualizar**: realiza a consulta o registro completo.  
  
**Salvar**: grava em um arquivo TXT os registros duplicados.  
  
**Imprimir**: gera um relatório com os registros duplicados.  
  
10. Após o término do processo, é recomendável executar a busca por duplicidades novamente. Se não houverem mais duplicidades, será exibida uma mensagem que **nenhum registro duplicado** foi encontrado.  
  
Observações:  
Para ambientes que tiverem o Gestão de Frotas habilitado (MV\_NGMNTFR = S), é necessário verificar a documentação abaixo para executar a rotina de Verificar Duplicidade (CheckDupl) corretamente:  
  
- UPDNGMNTFR - Chave para correta migração de versão do Protheus do SIGAMNT - Manutenção de Frotas  
Link: <http://tdn.totvs.com.br/pages/releaseview.action?pageId=59441499>  
  
- PROCEDIMENTO PARA MIGRAÇÃO DE FROTAS  
Link: <http://tdn.totvs.com.br/pages/releaseview.action?pageId=185750221>
