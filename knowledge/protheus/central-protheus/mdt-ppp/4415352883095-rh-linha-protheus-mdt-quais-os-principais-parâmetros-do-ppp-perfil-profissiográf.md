---
article_id: 4415352883095
category: MDT - PPP
content_hash: 35d9b33be4d3ce2fc4a08e6e10434e142465f990eb78b668e6e539bfa774e24b
fetched_at: '2026-06-28T22:44:22.266381+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus - MDT - Quais os principais parâmetros do PPP (Perfil Profissiográfico
  Previdenciário)
type: support-article
updated_at: '2025-03-12T14:18:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415352883095-RH-Linha-Protheus-MDT-Quais-os-principais-par%C3%A2metros-do-PPP-Perfil-Profissiogr%C3%A1fico-Previdenci%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20008733245463)** Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais os principais parâmetros do PPP (Perfil Profissiográfico Previdenciário)?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte: **[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)**Os principais parâmetros são:  
  
**MV\_PPPRISC =** Indica se o relatório PPP listara somente funcionários expostos a riscos ambientais. S=SIM / N=NAO.  
**MV\_MDTRESP** = Indica qual tabela será utilizada para selecionar Indica qual tabela sera utilizada para 1 - Funcionários (SRA) ou 2 - Usuários SESMT(TMK) selecionar   
**MV\_NG2SRIS** = Texto a ser impresso no PPP, caso o funcionário não esteja exposto a nenhum risco.   
**MV\_NG2KEPI** = Indica se a empresa utiliza EPI em caráter complementar, mesmo quando o EPC for eficaz. S=Sim ou N=Não   
**MV\_NG2M400** = Indica se a descrição das atividades do cargo terá todo o seu conteúdo impresso no PPP ou apenas será impresso os 400 primeiros caracteres. S=Sim;N=Não   
**MV\_NG2MEMP** = Indica se deve ser exibido na impressão do PPP do funcionário, o histórico em todas as empresas em que trabalhou. S=Sim;N=Não   
**MV\_NG2MFIL** = Indica se deve ser exibido na impressão do PPP do funcionário, o histórico em todas as filiais em que trabalhou. S=Sim;N=Não   
**MV\_NG2INVE** = Indica se deve ser trocado na impressão do PPP o conteúdo da coluna do Cargo com a coluna da Função S=Sim;N=Não   
**MV\_NG2CEPC** = Indica se a empresa consiste o EPC S=Sim, N=Não   
**MV\_NG2CEPI** = Indica se a empresa consiste o EPI S=Sim, N=Não   
**MV\_MDTDTFI** = Indica quais datas serão consideradas na impressão das seções do P.P.P. 1 - Responsáveis; 2 - Funcionários   
**MV\_PPPDTRI =** Quantidade de dias de tolerância que o funcionário poderá ficar sem receber o EPI, a partir do inicio de exposição a um agente de risco.   
**MV\_NG2PPPD** = "Data de corte para dados do PPP, onde nenhuma " "informação anterior a esta data será impressa."   
**MV\_NG2PPPC** = Se o CNPJ/CEI do C.C. do Funcionário estiver preenchido, indica se imprimirá o mesmo no P.P.P. ou o que estiver definido no arquivo de empresas. 1/2   
**MV\_REUTMAT** = Caso já exista a matrícula no destino da transferência em lote e individual, define se efetuará a (.T.) ou se a mesma não será realizada (.F.).   
**MV\_NG2MEAN** = Quantidade de meses antes da data de admissão do funcionário que os exames admissionais serão validos para o PPP. Informe de 1 ate 12.   
**MV\_NGMDTPS** = Indica se o cliente e um prestador de serviço de medicina S- Sim, N- Não.  
  
**Saiba Mais**[Artigos PPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050700933)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
