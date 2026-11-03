---
content_hash: d368b0b3aa1599e05d6cb17aadcd41bca737c39fbfae8acef6e9143c9237dc06
fetched_at: '2026-06-29T00:10:42.072706+00:00'
page_id: '546692138'
product: rm
source: tdn-rm
title: 13 - Solicitação de Recursos Didáticos - SESI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546692138
version: 26
---

|  |  |
| --- | --- |
| Descrição | Solicitação de Recursos Didáticos |
| Objetivo | O objetivo da solicitação de recursos didáticos é apoiar o ensino por meio da disponibilização de recursos didáticos. |

Os três caminhos seguem procedimentos distintos, no entanto, o procedimento sistêmico ocorre de forma semelhante

.

**Atividades de Processo:**

* *Solicitação de Atendimento*
* *Apropriar-se de um Atendimento*
* *Analisar a Solicitação e Avançar Etapa*
* *Encerrar o Atendimento (Solicitação Concluída)*

**Acesse:** Módulo TOTVS Aprovações e Atendimento | Novo Atendimento | Grupo de Atendimento: Secretaria | Tipo de atendimento: Solicitação de Recursos Didáticos

**Atendimentos | Parâmetros | Tipo de Recurso**: Escolher o Tipo de Recurso que está solicitando

## **Classificação da Solicitação**

**O processo está parametrizado no Sistema para permitir seguir três caminhos distintos no Workflow conforme descritos na MIT041 – Especificação de Processos do SESI, e****stes caminhos seguem conforme a classificação da solicitação:**

* **Recurso didático adequado**: Esta opção deverá ser selecionada pelo solicitante caso o material desejado exista na BRD (Base de Recursos Didáticos) e esteja tecnicamente adequado;
* **Recurso didático existente, mas não adequado:** Esta opção deverá ser selecionada pelo solicitante caso o material exista na BRD mas necessita ser adequado;
* **Recurso didático não existente:** Esta opção deverá ser selecionada pelo solicitante caso o material não exista na BRD.

## **O Workflow seguirá caminhos diferentes conforme Classificação da Solicitação:**

false

**1º Se a classificação da solicitação for igual a Recurso didático adequado**  
  
A Autorização para Reprodução e Distribuição do Recurso

O usuário deverá “Avançar Etapa” e o workflow será encaminhado para a fila do grupo de aprovadores onde um dos integrantes do grupo deverá “apropriar-se” do atendimento, que ficará sob sua responsabilidade nesta etapa.

**Deferido:** Após a autorização para reprodução e distribuição do recurso solicitado, o usuário responsável por esta etapa deverá encaminhar o workflow para o solicitante, para conhecimento. Neste momento, o workflow será devolvido para o solicitante com o status igual a concluído e um e-mail de notificação será enviado.

**Indeferido:** Caso a solicitação para reprodução e distribuição do recurso seja indeferida, o usuário deverá avançar o workflow para esta etapa. Neste momento, o workflow será devolvido para o solicitante com o status igual a concluído e um e-mail de notificação será enviado.

false

**2º Se a classificação da solicitação for igual a Recurso didático existente, mas não adequado:**   
  
**Análise para adequação do Recurso**: O usuário deverá “Avançar Etapa” e o workflow será encaminhado para a fila do grupo de aprovadores onde um dos integrantes do grupo deverá “apropriar-se” do atendimento, que ficará sob sua responsabilidade nesta etapa.

**Adequar recurso didático:** O usuário deverá “Avançar Etapa” e o workflow será encaminhado para a fila do grupo de aprovadores onde um dos integrantes do grupo deverá “apropriar-se” do atendimento, que ficará sob sua responsabilidade nesta etapa.

**Recurso didático adequado:** Após a adequação do recurso didático, o workflow será devolvido para o solicitante, para que o mesmo solicite a reprodução e distribuição do recurso didático.

**Autorização para Reprodução e Distribuição do Recurso:** O usuário deverá “Avançar Etapa” e o workflow será encaminhado para esta etapa, para o grupo de responsáveis cadastrado no sistema.

**Deferido:** Após a autorização para reprodução e distribuição do recurso solicitado, o usuário responsável por esta etapa deverá encaminhar o workflow para o solicitante, para que o mesmo tome ciência desta autorização. Neste momento, o workflow será devolvido para o solicitante com o status igual a concluído. O solicitante deverá receber um e-mail de notificação de conclusão.

**Indeferido:** Caso a solicitação para reprodução e distribuição do recurso seja indeferida, o usuário deverá avançar o workflow para esta etapa. Neste momento, o workflow será devolvido para o solicitante com o status igual a concluído. O solicitante deverá receber um e-mail de notificação de conclusão.

**Solicitar compra de Recurso:** Após a análise para adequação do recurso, caso não haja esta possibilidade, o workflow será encaminhado novamente para o solicitante, para que o mesmo encerre o workflow e realize o processo de compra definido em cada Unidade Operacional (no ERP local, conforme processo utilizado atualmente em cada UO).

Havendo possibilidade da aquisição do recurso didático, identificado como necessário para o curso/evento educativo, deve ser preenchida uma solicitação de compra a ser encaminhada ao setor responsável do DR, para providências de aquisição/compra do recurso, por meio do SGE.

false

**3º Se a classificação da solicitação for igual a Recurso didático não existente:**   
  
**Avaliar Solicitação:** A coordenação recebe e analisa a solicitação do Recurso. O usuário deverá “Avançar Etapa” e o workflow será encaminhado para a fila do grupo de aprovadores onde um dos integrantes do grupo deverá “apropriar-se” do atendimento, que ficará sob sua responsabilidade nesta etapa.

**Solicitar Compra de Recurso**: Após a análise para adequação do recurso, caso não haja esta possibilidade, o workflow será encaminhado novamente para o solicitante, para que o mesmo encerre o workflow e realize o processo de compra definido em cada Unidade Operacional (no ERP local, conforme processo utilizado atualmente em cada UO).   
  
Havendo possibilidade da aquisição do recurso didático, identificado como necessário para o curso/evento educativo, deve ser preenchida uma solicitação de compra a ser encaminhada ao setor responsável do DR, para providências de aquisição/compra do recurso, por meio do SGE.   
  
**Registrar demanda de desenvolvimento de material didático:** Após a análise da solicitação, caso o material não esteja disponível no repositório de conteúdos regionais e nacional (a ser desenvolvido), a decisão poderá ser o registro de demanda de desenvolvimento de material didático. Neste caso, o workflow deverá ser encaminhado para a área técnica, para consolidação de uma proposta a ser registrada para o administrador do repositório de conteúdos regionais e nacional (a ser desenvolvido). O solicitante receberá um e-mail informando que o recurso será elaborado e um prazo estimado para o atendimento.

**Após a elaboração do Recurso Didático o Workflow será concluído e o solicitante deverá receber um e-mail com estas informações**

[Sistema Indústria](https://tdn.totvs.com/pages/releaseview.action?pageId=527384229)
