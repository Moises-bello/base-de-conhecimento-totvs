---
article_id: 1500010835662
category: Relatórios
content_hash: f4518d922af7e8bd6600e6227925fc9d631a6f685e4d0181de1a5b830a936389
fetched_at: '2026-06-28T22:47:43.462560+00:00'
product: rm
section_id: 1500000861522
source: central-rm
title: 'RH - RM - SMT - Erro ao gerar relatório PPP: Inconsistência no histórico de
  seção'
type: support-article
updated_at: '2026-06-02T18:34:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010835662-RH-RM-SMT-Erro-ao-gerar-relat%C3%B3rio-PPP-Inconsist%C3%AAncia-no-hist%C3%B3rico-de-se%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035997339415) Tempo aproximado para leitura: 00:00:15 min**

**Ocorrência**  
Ao gerar o relatório PPP (Perfil Profissiográfico Previdenciário) é apresentado erro:  
  
GERANDO PPP PARA CHAPAXXXXX  
...Configurações iniciais executadas.   
...Dados administrativos processados.   
...Dados da CAT processados.   
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
ERRO NA GERAÇÃO DO RELATÓRIO: Inconsistência no histórico de seção. Favor verificar.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional – Todas as Versões  
  
**Causa**  
Este incidente ocorre devido a alguma inconsistência no(s) histórico(s) do(s) funcionário(s).  
  
**Solução**  
Para solucionar essa ocorrência, valide para o(s) funcionário(s) em questão se há registro no Histórico de Seção dos Colaboradores correspondente a data de Admissão deles. Abaixo segue os passos de como realizar a verificação:

1 - Acessar o cadastro do funcionário, editá-lo, e na guia **Registro** avaliar o campo **Data de Admissão**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40918788574871)

2 - Em seguida acessar o histórico de seção através da opção de Anexos | Históricos | Histórico de Seção:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40918788576407)  
  
3 - Edite o registro do histórico e verifique o campo **Data da Mudança**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40918788578199)  
​

4 - Caso o(s) Funcionário(s) tenha(m) sido transferido(s), no Histórico de Seção deverá existir registro com a mesma data da transferência. Para verificação poderá acessar o cadastro do funcionário, guia **Registro** e campo **Data da Transferência**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40918778743063)​  
  
Avalie o cenário conforme os exemplos acima e se necessário inclua no Histórico de Seção o registro faltante com sua respectiva data ou altere o registro já criado para a data correta. ​A inclusão é de forma manual. Após isso gere o relatório novamente.  
  
**Saiba Mais**

Para maiores informações, acesse:

- [RH - RM - SMT - Como gerar o Relatório PPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000240188)
