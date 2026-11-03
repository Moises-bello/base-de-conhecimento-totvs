---
article_id: 360038454074
category: Controle de Documentos (SIGAQDO)
content_hash: 76f132f21e7b9d72e02070e5af4e8fa9815533d693aa2b55d74b99434811af95
fetched_at: '2026-06-28T22:42:29.195229+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Integração entre SIGAGPE e Protheus
  Qualidade
type: support-article
updated_at: '2025-09-29T23:13:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038454074-Manufatura-Linha-Protheus-SIGAQDO-Integra%C3%A7%C3%A3o-entre-SIGAGPE-e-Protheus-Qualidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:15 min**  
 **Dúvida**Como habilitar a integração entre o módulos do **Protheus Qualidade** e **Protheus Gestão de Pessoal - SIGAGPE**?  
  
 **Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Para que os módulos do **Protheus Qualidade** utilizem os mesmos cadastros de **Usuários** e **Funções** já existentes no módulo **Gestão de Pessoal - SIGAGPE** e também utilize o mesmo cadastro de **Centro de custo** de **Contabilidade - SIGACTB** para o cadastro de Departamentos, é necessário realizar os passos a seguir:  
 **1.** Realizar *backup* completo do banco de dados e também do dicionário de dados - **tabela SX3**.  
 **2.** Configurar o parâmetro **MV\_QGINT - Indica se os modulos Quality estão integrados com Módulo SIGAGPE e não habilita a opção de INCLUIR**igual à **S - Sim**;  
 **3.** Verificar se o compartilhamento entre as tabelas **SRA - Funcionários** e **QAA - Usuários**, **CTT - Centros de Custos** e **QAD - Departamentos**, e **SRJ - Funções** e **QAC - Cargos e Funções** está equivalente. Isto é, a tabela **QAA** é exclusiva e consequentemente a tabela **SRA** também precisa estar em modo exclusivo. O mesmo se aplica para as demais tabelas mencionadas.  
**4.** Acessar o módulo **SIGACFG - Configurador**, menu **Cadastros** > **Menus** e adicionar a rotina **RHTOQUA** em um módulo qualquer, para ser acessado posteriormente. Em caso de dúvidas neste passo, acesse ao artigo disponível na seção **Saiba mais.**  
**5.** Acessar o módulo onde foi adicionado o menu **RHTOQUA** e aguardar a execução da rotina.   
**5.1.** Caso a rotina **RHTOQUA** já tiver sido executada anteriormente, é necessário acessar a tabela **SX6 - Parâmetros** via **APSDU** e apagar o parâmetro **MV\_QRHTOQA - Define se houve atualização das tabelas do quality apos migração de versão**.  
**5.2.** Caso a rotina **RHTOQUA** identifique algum campo com tamanho inconsistente, será apresentado em tela o nome do campo para que seja realizado o ajuste. Neste caso, abra a tabela **SX3** através do **APSDU**, localize os campos informados e altere o conteúdo do campo **X3\_CAMPO** para o tamanho correto. Após ajuste dos campos, execute a rotina **RHTOQUA** novamente.  
**6.** Após o término da execução, remover a rotina **RHTOQUA** do menu e validar se as informações foram atualizadas nas tabelas **QAA, QAD e QAC**.  
  
**Importante  
1.**A integração entre os ambientes permite a independência do **Cadastro de Usuários**, **Funcionários**, **Departamentos/Centros de Custos** e de **Funções/Cargos**.   
**2.**Não recomendamos a ativação do parâmetro **MV\_QGINT** quando o Sistema já estiver em uso. Ao executar o programa **RHTOQUA** todas as informações dos cadastros citados neste documento são copiadas para as tabelas do **Protheus Qualidade**. Porém, as informações já cadastradas nas tabelas de **Qualidade** não serão replicadas para as tabelas do **SIGAGPE**, podendo gerar inconsistência nos registros já existentes. Caso mesmo assim desejar habilitar a integração, recomendamos que realize testes inicialmente em seu ambiente de homologação.   
**3.** Recomendamos que configure o parâmetro **MV\_QVLUSAR** **- Preencha com 1 para que o sistema verifique as tabelas do ambiente Quality na execução da transferência de funcionários. Senão, informe 2.** como **1**.  
**4.** O cadastro de **Departamento** dos módulos da **Qualidade**, não se relaciona com o cadastro de **Departamentos** do **Gestão de Pessoal**. O relacionamento é realizado através da tabela **CTT - Centros de Custos**.

**Saiba mais**  
Para mais informações sobre como executar o **passo 4** do tópico **Solução**, verifique o procedimento disponível no link [MP - FRAME - Personalização de Menus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000575567-MP-FRAME-Personaliza%C3%A7%C3%A3o-de-Menus)
