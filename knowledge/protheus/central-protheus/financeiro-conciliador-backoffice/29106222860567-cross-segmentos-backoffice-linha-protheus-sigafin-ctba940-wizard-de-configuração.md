---
article_id: 29106222860567
category: Financeiro - Conciliador Backoffice
content_hash: a93674fe90749c827ecd3d280c038ce8b05fa34e1685b6dc32d66fefe1887600
fetched_at: '2026-06-28T22:37:47.241760+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - WIZARD de
  configuração do Novo Conciliador Backoffice
type: support-article
updated_at: '2025-08-14T19:10:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29106222860567-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-WIZARD-de-configura%C3%A7%C3%A3o-do-Novo-Conciliador-Backoffice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29106222839063) Tempo aproximado para leitura: **00****:15:00 min****Dúvida:**Como executar o WIZARDUUID de configuração do novo Conciliador Backoffie?  
  
**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução:**Para solucionar essa dúvida, realize os seguintes passos:  
1. Antes de executar o **Wizard**, ative o parâmetro **MV\_PRJOVER** nos grupos de empresa desejados.  
No campo de conteúdo, preencha com **“.T.”**, conforme o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188823572247)

2. Baixar o pacote de atualização de dicionários atual (backoffice) necessários para implementação do Conciliador e executar o UPDDISTR. O pacote de dicionário deverá criar em seu banco de dados as tabelas **QLB, QLC** e **QLD:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188823575831)

Com o parâmetro **MV\_PRJOVER** ativado, será possível a inclusão de campos de identificação única (MSUIDT) nas tabelas que serão conciliadas.

Portanto, se este for o primeiro uso do Conciliador, acesse primeiramente a rotina **Conciliador Backoffice (CTBA940)** no menu do Protheus para que as configurações de *Match* sejam carregadas em seu ambiente. Somente após essa etapa, retorne ao **WIZARDUUID** para prosseguir com os passos seguintes.

3. Para usar o Assistente de Configurações, é necessário especificar o programa inicial: **WIZARDUUID.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188823584279)

4. Ao confirmar a tela anterior, a tela de apresentação do WIZARD será apresentada:

Apenas o **usuário administrador** possui permissão para acessar o ambiente por motivos de segurança.  
Após informar a senha, clique em  "Avançar".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188823587479)

5. Escolha os conjuntos de empresas que pretende usar no processamento e pressione '**Avançar'**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188794132247)

6. Após abrir a tela, as opções disponíveis para processamento serão apresentadas.

O conciliador oferecerá três alternativas para ajudar na configuração inicial da base de dados.

**🚩️ Importante:**

Foi implementada uma melhoria que importa automaticamente as configurações de *Match* (QLB) ao acessar o Conciliador. Por isso, a primeira opção do *Wizard* foi descontinuada e está desabilitada.  
Não é mais necessário executá-la — basta acessar a rotina **CTBA940** no menu do Protheus para que as configurações de *Match* sejam importadas para a tabela **QLB**.

7. Siga todas as etapas disponíveis do Wizard conforme a sequência apresentada no momento de implantação, **não pule etapas para não ocorrerem erros no processo.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188794134423)

Após ter realizado seu primeiro acesso à rotina Conciliador Backoffice para o carregamento das configurações de match, siga a sequência:

* Gerar SDF com os campos de ID
* **Popular os campos de ID (opcional)**
* **Popular Rastreamento Contábil (opcional)**

**🚩️ Importante:**

A opção **"Popular Rastreamento Contábil"** não será tratada neste artigo, pois os rastreamentos contábeis são utilizados apenas nas configurações contábeis (contabilizações, processos de 0001 à 0021) e não fazem parte das conciliações bancárias.

Da mesma forma, a opção **"Popular os Campos de ID"** será abordada em outro artigo, visto que os registros conciliados nas rotinas anteriores não precisam ser integrados à nova rotina. Essas alternativas são opcionais e, por essa razão, não serão tratadas aqui.

8. Escolher a opção **"Gerar SDF com campos de ID"** e clicar no botão Avançar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188823592343)

9. Será exibida a tela de apresentação da opção selecionada:![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188823593751)

Ao clicar em **Prosseguir**, o sistema fará a leitura das tabelas de origem e destino registradas na tabela **QLB** (Configurações de Match). Nessa etapa, será proposta a criação dos campos **XXX\_MSUIDT** nessas tabelas, onde **XXX** representa o código da tabela identificada.

As tabelas utilizadas pelos processos bancários são: **FK5 e SIG.**

Os campos já presentes na base de dados permanecerão com o **Situação = "OK"** e não serão transferidos para o SDF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188794138263)

Os campos que não foram encontrados serão exibidos com o **Situação = "Incluir"** e serão exportados para o **arquivo SDF**. Estes campos serão criados com base nas tabelas encontradas no cadastro da QLB:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188823596695)

10. Selecione a opção **Exportar** para transferir o arquivo **SDF** para a pasta *systemload*.  
Caso já exista um arquivo diferencial nessa pasta, o sistema exibirá uma mensagem perguntando se deseja sobrescrever o arquivo existente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188823600919)

11. Exemplo de arquivo criado na pasta systemload.

Evidência do arquivo manifest\_update com os detalhes do arquivo SDF gerado pela ferramenta

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29107108406551)

12. Após confirmar a gravação do arquivo, o **Wizard apresenta a notificação de SDF exportado com êxito**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34188823602455)

Ao selecionar a opção **"finalizar"**, o sistema questiona se deseja realizar o **UPDDISTR** para a criação dos campos, somente após a finalização do UPDDISTR os campos serão efetivamente alterados para **"Situação = OK"**

13. Se clicar em **“Sim”**, o sistema redirecionará para execução do **UPDDISTR**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29107108414615)

14. Ao finalizar esta etapa do Wizard, a mensagem de Processamento Finalizado é exibida:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29107108423447)

**Saiba mais**

[Conciliador Backoffice - Configuração e Instalação](https://tdn.totvs.com.br/pages/releaseview.action?pageId=638741736)
