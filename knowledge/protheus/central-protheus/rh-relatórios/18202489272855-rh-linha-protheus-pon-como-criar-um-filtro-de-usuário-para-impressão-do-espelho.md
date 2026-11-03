---
article_id: 18202489272855
category: RH - Relatórios
content_hash: 59ef33a105fdda66bb93d8c65fbe4939cd4d9bba8b9268ec5dc1b9d798457b8a
fetched_at: '2026-06-28T22:44:43.451618+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Como criar um filtro de usuário para impressão
  do Espelho de Ponto por Centro de Custo
type: support-article
updated_at: '2025-10-08T17:13:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18202489272855-RH-Linha-Protheus-PON-Como-criar-um-filtro-de-usu%C3%A1rio-para-impress%C3%A3o-do-Espelho-de-Ponto-por-Centro-de-Custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18202542443415) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como criar um filtro de usuário para impressão do Espelho de Ponto por Centro de Custo?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) Ponto Eletrônico - Todas as versões  
  
**Solução**Para criar uma restrição para impressão de **Espelhos de Ponto** de um **Centro de Custo específico**, seja para um Usuário ou para um Grupo de Usuários, pode ser usada a rotina **Controle de Acesso de Usuário**, seguindo os passos descritos abaixo:

**1.** Acessar o módulo **07 - Gestão de Pessoal** na rotina **Controle de Acesso de Usuário** pelo caminho **Atualizações> Cadastros> Controle de Acesso de Usuário** e clique em **Incluir:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18203159944599)

**2.** Preencha os campos conforme a definição de restrição desejada:  
**- Grupo Usuari (RW\_GRUPO)** = se a restrição se aplicar para um grupo específico, informe o código deste grupo  
**- Id Usuário (RW\_IDUSER)** =se a restrição se aplicar para um usuário específico, informe o código do usuário  
**- Arquivo (RW\_ALIAS)** = informe a tabela que deseja realizar o filtro   
**- Processo (RW\_PROCESS)** = informe o fonte da rotina que deseja realizar o filtro  
**- Descrição (RW\_DESCRI)** = nome do processo/rotina que terá o filtro  
**- Filtro Brows (RW\_FILBROW)** = expressão que vai fazer o filtro no arquivo (tabela) informado no campo **Processo**  
- **Filtro Relat (RW\_FILREL)** = expressão que vai fazer o filtro no arquivo (tabela) informado no campo **Processo****- Validação (RW\_VALID)** = informe uma expressão para filtrar os dados do processo (fonte)   
  
Segue abaixo exemplo das configurações para um **usuário**:  
Processo **PONR010** referente a rotina **Espelho de Ponto,** permitindo acesso somente nos Centros de Custos 000000002 e 000000003:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18206254182807)

**3.** Após realizar as definições dos filtros na rotina **Controle de Acesso Usuários**, acessar o modulo **16 - Ponto** **Eletrônico** na rotina **Relatórios> Mensais> Espelho de Ponto,** e veja que será gerado o **Espelho de Ponto** somente dos **Centro de Custos** definido para o usuário especificado no controle de acesso:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18206535425047)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18206498690071)

**Observação:** Mesmo definindo o filtro na rotina **Controle de Acesso Usuário**, ao realizar o preenchimento dos parâmetros para impressão do **Espelho de Ponto** serão apresentados **todos os Centros de Custos** cadastrados no sistema, pois esse campo é abastecido pela tabela **CTT**.   
A tabela **CTT** é de domínio da controladoria, sendo assim a rotina de **Controle de Acessos** não tem controle sobre esta tabela, mas o relatório **não será impresso** para Centros de Custos que o **usuário não tem acesso.  
  
  
  
Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
