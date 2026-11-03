---
article_id: 40110965723415
category: Relatórios
content_hash: efac157ca25b9ce2d193d6d47efc9ad1af3629fb074baa1b99ebb107c52440ba
fetched_at: '2026-06-28T22:47:43.360328+00:00'
product: rm
section_id: 1500000861522
source: central-rm
title: 'RH - RM - SMT - Erro ao gerar relatório PPP: Input string was not in a correct
  format'
type: support-article
updated_at: '2026-04-30T16:02:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40110965723415-RH-RM-SMT-Erro-ao-gerar-relat%C3%B3rio-PPP-Input-string-was-not-in-a-correct-format
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40110941926679) Tempo aproximado para leitura: **00:08:00 min**  
  
**Ocorrência**  
Ao gerar o relatório PPP (Perfil Profissiográfico Previdenciário) no módulo de Segurança e Saúde Ocupacional (SSO) da linha RM, a seguinte mensagem de erro é apresentada:

GERANDO PPP PARA CHAPAXXXXX  
...Configurações iniciais executadas.  
...Dados administrativos processados.  
...Dados da CAT processados.  
...Informações da lotação processadas.  
...Profissiografia processada.  
...Exposições a riscos processadas.  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
ERRO NA GERAÇÃO DO RELATÓRIO: Verifique se os históricos do funcionário estão corretos  
Input string was not in a correct format.  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional – Todas as Versões  
  
**Causa**  
Este erro ocorre devido a ausência do documento de Cadastro de Pessoas Físicas (CPF) no registro de Pessoa do(s) Responsável(s) pelo(s) Registro(s) Ambiental(s) e/ou do(s) Responsável(s) pela Monitoração Biológica.  
  
**Solução**  
Para solucionar essa ocorrência, valide para cada Responsável Ambiental e Biológico se o cadastro de Pessoa destes profissionais possuem o campo CPF preenchido na guia Doc. Básicos. Abaixo seguem os passos para validação e ajuste.

1 - Acesse o cadastro de Responsáveis pelos Registros Ambientais através da guia PPRA/PGR | menu Resp. Reg. Ambientais. Aplique um filtro que retorne todos os Registros.

![Filtro_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40110941928087)

2 - Após a aplicação do filtro, valide para cada cadastro de Responsável Pelos Registros Ambientais, se o registro de Pessoa do responsável possui o campo CPF preenchido. Para acesso direto ao cadastro de Pessoa clique sobre o nome do responsável, dessa forma o sistema abrirá o cadastro correspondente. Acesse a guia Doc. Básicos do menu lateral esquerdo dentro do grupo Dados Pessoais e valide se o CPF está preenchido. Caso não esteja deverão preencher o campo e salvar a alteração.

![Ambiental.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40110941929751)

3 - Da mesma forma efetuem as validações também no cadastro dos Responsáveis pela Monitoração Biológica. Para isso acesse o cadastro de Responsáveis pela monitoração através da guia PCMSO | menu Resp. Monitoração Biológica. Aplique um filtro que retorne todos os Registros.

![Filtro_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40110965707287)

4 - Após a aplicação do filtro, valide para cada cadastro de Responsável pela Monitoração Biológica, se o registro de Pessoa do responsável possui o campo CPF preenchido. Para acesso direto ao cadastro de Pessoa clique sobre o nome do responsável, dessa forma o sistema abrirá o cadastro correspondente. Acesse a guia Doc. Básicos do menu lateral esquerdo dentro do grupo Dados Pessoais e valide se o CPF está preenchido. Caso não esteja deverão preencher o campo e salvar a alteração.

![Biológico.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40110965709591)

**Saiba Mais:**

Para mais informações, acesse:

[PPP – Perfil Profissiográfico Previdenciário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719230)
