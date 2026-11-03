---
article_id: 360021565472
category: RH - Cadastros
content_hash: cdabdcca1faf0892dadc3c098e5b1020e6618482f28b219def1d9d6e770e1133
fetched_at: '2026-06-28T22:43:25.907787+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração para Impressão de Documentos no Word
  (GPEWORD)
type: support-article
updated_at: '2026-06-25T10:58:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021565472-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-Impress%C3%A3o-de-Documentos-no-Word-GPEWORD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591707927) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**  
Como configurar o sistema para impressão de documentos *Word?*  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

O programa **GPEWORD** deverá ser utilizado para impressão de **Documentos** através do***Microsoft Word.***

Efetue as etapas discriminadas a seguir para tratamento das variáveis e impressão do Contrato de Trabalho, por exemplo:

1. Para verificar as variáveis disponíveis, acesse no menu do SIGAGPE as opções **Atualizações > Integrações > Word**  
  
2. Clique em **Impr. Variáveis** e depois em **Ok**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494577783703)

3. Será apresentado em tela as variáveis disponíveis para utilização no modelo de contrato.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591723927)  
  
Assim como outros relatórios, o Sistema permite a impressão externa ou em PDF.

4. Abra a página do ***Word***para digitar a estrutura do documento:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591728919)

5. Posicione o cursor do mouse ao lado da Variável **NOME,** selecione o menu **Incluir > Partes rápidas > Campo**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591732631)  
  
  
6. Na tela seguinte, informe:  
  
**Categoria:** Automação de documento  
**Nomes dos campos:** DocVariable  
**Novo nome:** GPE\_NOME (variável de acordo com a listagem apresentada no item 3 acima).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494577805591)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494577810327)

Realize o mesmo procedimento para as demais variáveis que forem necessárias para o modelo de contrato.

7. Depois de incluir as variáveis para os campos que precisa buscar dados so Sistema, salve ao arquivo com extensão **.dot** ou **.dotx**no diretório desejado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591754519)

8. Para impressão do documento, selecione na rotina **Word** a opção parâmetros e preencha de acordo com a necessidade.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494577821463)

No exemplo abaixo, faremos a impressão de uma matrícula apenas que foi admitida em 2024 no formato PDF, uma vez que a impressora padrão selecionada éa PDF.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591766807)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494577830551)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591772311)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591778327)

**Importante**: Para o campo **Arquivo do Word**, selecione na **lupa** o arquivo **.dot** salvo e já configurado anteriormente (itens de 4 até 7 acima mencionados).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591781143)

Para o **Arquivo Saída**, observe que foi informado o**C**: da máquina do operador que irá gerar a impressão do contrato de trabalho e após o caracter \ o nome do **arquivo.DOC.** Esta informação deve ser **digitada** pelo usuário ao clicar na **lupa** e selecionar diretóirio **C:.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591786647)

9. Após o preenchimento dos parâmetros, clique em **Ok** e depois **Impr.Documento**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591788951)  
  
O Sistema abrirá o arquivo .dot em modo de compatibilidade em segundo plano e abrirá uma nova tela para salvanto do arquivo em formato PDF.  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591790871)**

Após clicar em **Salvar**, o arquivo .dot será fechado e os arquivos de saída gerados nos diretórios selecioandos.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591792279)

Exemplo do de contrato gerado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26494591798167)

**Importante**: Caso algum item do documento venha sem informação, como no exemplo acima, verifique se existe a informação cadastrada no Sistema.

**DICA:**Para conferir/visualizar as variáveis inseridas no documento WORD:

1. Abrir o arquivo que possui ou está sendo inserida as variáveis
2. Selecionar o texto
3. Clica com o botão direito do mouse
4. Seleciona a opção: “ALTERNAR CÓDIGOS DE CAMPOS”
5. O documento apresenta as variáveis
6. Após consulta ou alteração, selecionar novamente o texto, clicar com o botão direito do mouse, selecionar a opção “ATUALIZAR CAMPO”

![variaveis word.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26761733695639)

**Atenção:**Na rotina **GPEWORD,** ao parametrizar existe a pergunta **Verific. Dependente,** então quando informada **NÃO,** o sistema traz todos os funcionários em geral. Se for informado **SIM** irá considerar para impressão apenas os colaboradores que contenham dependentes.

**Saiba Mais**  
[RH - Linha Protheus - GPE - O que verificar quando o GPEWORD não funciona](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40065914922647-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-GPEWORD-n%C3%A3o-funciona)  
[RH - Linha Protheus - GPE - Variáveis que podem ser usadas na Integração com o WORD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010260602-RH-Linha-Protheus-GPE-Vari%C3%A1veis-que-podem-ser-usadas-na-Integra%C3%A7%C3%A3o-com-o-WORD?source=search)  
[RH - Linha Protheus - GPE - Ao gerar a integração com WORD, de várias matrículas, é salvo apenas a última matrícula no arquivo de saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025940474-RH-Linha-Protheus-GPE-Ao-gerar-a-integra%C3%A7%C3%A3o-com-WORD-de-v%C3%A1rias-matr%C3%ADculas-%C3%A9-salvo-apenas-a-%C3%BAltima-matr%C3%ADcula-no-arquivo-de-sa%C3%ADda?source=search)  
[RH - Linha Protheus - GPE - Integração com o Word apresenta mensagem: Não conseguimos encontrar seu arquivo. É possível que ele tenha sido movido, renomeado ou excluído](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052139513-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-com-o-Word-apresenta-mensagem-N%C3%A3o-conseguimos-encontrar-seu-arquivo-%C3%89-poss%C3%ADvel-que-ele-tenha-sido-movido-renomeado-ou-exclu%C3%ADdo?source=search)
