---
article_id: 18315122447895
category: SIGAEST - CUSTOS
content_hash: b8e6b5974ffc1158068568f4d6849b3189d611c5a016abc3fae2da6621553230
fetched_at: '2026-06-28T22:39:00.916827+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro instalação procedure
  19 - Open index error: TRB01SP on A330CRTABS(MATA330.PRX)'
type: support-article
updated_at: '2025-03-12T12:26:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18315122447895-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-instala%C3%A7%C3%A3o-procedure-19-Open-index-error-TRB01SP-on-A330CRTABS-MATA330-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18315126516375) Tempo aproximado para leitura: **04:30:00 min****Dúvida**Ao efetuar o processo de reinstalação ou instalação da procedure 19, ocorre o erro: Open index error: TRB01SP, como corrigir?  
  
**Ambiente**

Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Todas as versões.

**Solução**

O erro "Open index error: **TRB01SP (numero do indice)** on A330CRTABS(MATA330.PRX)" indica que o sistema encontrou um problema ao tentar abrir um índice chamado "TRB01SP11" na função arquivo "A330CRTABS" com base na estrutura de índices definida no arquivo de programa "MATA330.PRX".

Esse erro geralmente ocorre quando o índice não está disponível ou não pode ser aberto devido a alguma customização incorreta ou ausência do índice padrão.

**Para corrigir esse erro, siga as etapas a seguir:**

1. **Verificação do Índice Padrão:**

Primeiro, você deve verificar se o índice "TRB01SP**11**" é um índice padrão do sistema ou se foi criado como uma customização, para esse exmplo, datado em **2023/10/16** a tabela TRB possui somente 10 indices, ou seja o indice 11 não é padrão.

2. **Exemplo de Como Avaliar se o Índice é Padrão:**

Aqui está um exemplo de como avaliar se o índice é padrão ou personalizado:

**a)** Em contato com o suporte técnico para determinar se o índice "TRB01SP11" faz parte dos índices padrão do sistema.

**b)** Você pode listar todos os índices disponíveis no arquivo "TRB01SP" usando um comando ou função que lista os índices do arquivo. Por exemplo, se estiver trabalhando com uma linguagem de programação como Progress OpenEdge, você pode usar o comando `SHOW INDEXES` ou `INDEX-NAME` para listar os índices disponíveis, ou então via SQL com o comando:

**SELECT \* FROM sys.indexes WHERE name LIKE ('%TRB%')**

**Exemplo do resultado:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18314949340183)**

3. **Verificação de Customizações Relacionadas:**

Se for determinado que o índice "TRB01SP11" não faz parte dos índices padrão do sistema, você deve verificar se há alguma customização relacionada a esse índice. Normalmente, customizações são feitas nos programas de aplicação (pontos de entrada) ou nas definições de índice (tabela SIX)

4. **Exemplo de Como Verificar Customizações:**

**a)** Examine o código-fonte do programa "SEUFONTECUSTOMIZADO.PRW" em busca de qualquer referência ao índice "TRB01SP11". Verifique se há alguma linha de código que cria, modifica ou usa esse índice.

**b)** Verifique se existe algum arquivo de dicionário de dados ou configurações relacionadas a índices personalizados. É importante revisar as definições de índices no dicionário de dados e garantir que o índice "TRB01SP11" tenha sido definido corretamente, se aplicável.

5. **Reavaliação da Customização:**

Se você encontrar customizações relacionadas ao índice "TRB01SP11", revise cuidadosamente as configurações e o código para garantir que a customização esteja correta. Se houver algum erro ou inconsistência na criação ou uso desse índice personalizado, faça as correções necessárias.

Lembre-se de que, em muitos casos, é aconselhável trabalhar com um desenvolvedor experiente ou um especialista no sistema para ajudar na identificação e correção de problemas relacionados a índices e customizações, especialmente se a customização for complexa.

Certifique-se de fazer backup de seus dados e customizações antes de fazer alterações significativas no sistema.

**Saiba mais:**

**[Stored Procedures utilizadas no produto Estoque e Custos](https://tdn.totvs.com/x/wi3AFQ)**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
