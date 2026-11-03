---
article_id: 9340088026519
category: RH - Integrações
content_hash: 4c0eb75b9c9c10596d1196f55f0282cb8c3485bb166990cc01db9eb8681b7ef5
fetched_at: '2026-06-28T22:44:47.582817+00:00'
product: protheus
section_id: 32419269542935
source: central-protheus
title: RH - Linha Protheus - PON - Integração Espelho de Ponto x TAE
type: support-article
updated_at: '2026-02-11T20:02:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9340088026519-RH-Linha-Protheus-PON-Integra%C3%A7%C3%A3o-Espelho-de-Ponto-x-TAE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32125854455831) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como realizar a integração do Espelho de Ponto com o TAE (TOTVS Assinatura Eletrônica)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Foi implementada a possibilidade de **integração do relatório de Espelho de Ponto com o TAE** (TOTVS Assinatura Eletrônica). Para isso, é necessário seguir os passos abaixo:  
  
**1-** No Cadastro de Funcionário, via **SIGAPON,** em **Atualizações> Cadastro de Funcionários> Funcionários**, na Aba Cadastros ter um **endereço de E*****mail*** **Princ vinculado ao Cadastro do Funcionário** no Protheus;  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9339572394903)  
  
  
**2-** Ter um **usuário no TAE** com **permissão para** ***upload*** de arquivos. Sobre cadastro de acesso a plataforma acesse o [Manual Operacional TOTVS Assinatura Eletrônica](https://tdn.totvs.com/x/fvccJ)  
  
  
**3-** Criar o parâmetro **MV\_SIGNURL** e preencher seu conteúdo de acordo com o exemplo abaixo (o conteúdo se trata da URL padrão da plataforma):  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9339269308567)  
  
  
**4-** No SIGAPON, acessar o menu **Atualizações> Lançamentos> Controle de Espelho de Ponto** clicar em **Outras Ações / Config. Assina. Eletr:**  
**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9339668028567)**  
  
  
Informar o **usuário e senha do TAE** que **tenha permissão de** ***upload*** na plataforma:  
**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9339684602647)**  
  
  
**OBS:** para verificar se o usuário tem **permissão de** ***upload*** no TAE, **acesse a ferramenta neste** ***link*****:**<https://totvssign.totvs.app/webapptotvssign/#/auth> e realize o *login* com o **mesmo usuário e senha** informados na rotina **Controle de Espelho de Ponto**. Na tela do TAE deverá aparecer a opção de **Adicionar Documentos**:  
![](https://tdn.totvs.com/download/attachments/664181206/image2022-7-13_16-12-19.png?version=1&modificationDate=1657739540367&api=v2)

**5-** Nos **parâmetros da impressão** do **Espelho de Ponto**, a **pergunta "Integrar TAE?"** deve estar como **Sim**:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9339792041751)  
  
  
Será gerado um **Log de Ocorrências** da **integração do Espelho com o TAE**, informando **se o arquivo foi ou não enviado** à plataforma:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9339795647127)  
  
  
Consultando no TAE, o **documento** estará com *status* **Pendente** **para assinatura**:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9339797272087)  
  
  
Na rotina de **Controle de Espelho de Ponto** também é possível **visualizar** o **documento Pendente de assinatura.**  
**Para documentos com este** ***status*****, é habilitado um** ***grid*** **com quatro opções:**  
**- Excluir Documento =** o documento será excluído **permanentemente do SIGAPON e do TAE**. A ação **não pode ser revertida**;  
***- Download =*** baixar o **arquivo pendente de assinatura**;  
**- Verificar Assinatura =** esta opção **valida** se o funcionário em questão **assinou recentemente o Espelho de Ponto no TAE**, se **sim**, o *status* é **alterado para "Devolvido";**  
- **Solicitar Assinatura =** é feito o **reenvio do** ***email*** para o funcionário, alertando sobre o documento pendente de assinatura.  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9339872845719)  
  
  
  
Após o **documento ser assinado no TAE** e ser feita a **Verificação de Assinaturas**, o *status* é **alterado** para **"Devolvido":**  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9339990136983)  
  
  
  
**OBS:** na rotina **Controle de Espelho de Ponto**, clicando em **Outras Ações / Verificar Assinaturas**, é feita a **mesma varredura de assinaturas recentes** em documentos, porém, de forma **coletiva** para todas as matrículas da base. Após o processamento, é gerado um **Log de Ocorrências** detalhando os **novos documentos assinados**:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9339973696279)  
  
  
  
  
**Saiba mais:**  
**How To:** <https://www.youtube.com/watch?v=YW_elyeHz24>  
**Manual do Ponto:** <https://tdn.totvs.com/pages/releaseview.action?pageId=630823373>  
Integração TAE no espelho de Ponto-<https://tdn.totvs.com/pages/releaseview.action?pageId=664181206>  
[Manual Operacional TOTVS Assinatura Eletrônica](https://tdn.totvs.com/x/fvccJ)
