---
article_id: 360051276674
category: RH - Benefícios
content_hash: 48504a543fa22148f9a3f7940d5ef012643c4e61a115faf8487f47380ce28c2d
fetched_at: '2026-06-28T22:44:03.801240+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona a hierarquia do cálculo automático
  de benefícios
type: support-article
updated_at: '2025-09-15T11:15:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051276674-RH-Linha-Protheus-GPE-Como-funciona-a-hierarquia-do-c%C3%A1lculo-autom%C3%A1tico-de-benef%C3%ADcios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32615436786967) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como funciona a hierarquia do cálculo automático de benefícios?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**

O cadastro de Critérios de Benefícios define a ordem que o sistema irá utilizar para definir quais benefícios o funcionário tem direito.  Definida a ordem, basta vincular os benefícios às entidades e executar o cálculo.  
  
A primeira entidade é fixa e sempre será o funcionário, dessa forma garantimos que os benefícios vinculados diretamente ao funcionário (utilizando a rotina de atualização de benefícios - Tabela SM7), será sempre respeitado.  
  
Caso o funcionário se encaixe em mais de um critério será calculado o primeiro encontrado, respeitando essa ordem.  
  
Veja o exemplo abaixo:  
O funcionário está alocado no centro de custo **02**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080447374)  
  
No lançamento do benefício, o cadastro segue a seguinte forma:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080606734)  
  
O fato do cadastro acima estar com o centro de custo 02, o cálculo do benefício será executado para todos os funcionários alocados no centro de custo 02![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081657573)  
  
Caso o funcionário cumpra os dois critérios será calculado apenas o vale definido primeiro, pois a entidade tem maior prioridade.  
  
Estão disponíveis Doze entidades para serem utilizadas no cadastro, sendo elas:

| Entidade | Tabela | Campo Chave |
| --- | --- | --- |
| Funcionário | SRA | RA\_MAT |
| Departamento | SQB | QB\_DEPTO |
| Centro de Custo | CTT | CTT\_CUSTO |
| Posto | RCL | RCL\_POSTO |
| Cargo | SQ3 | Q3\_CARGO |
| Função | SRJ | RJ\_FUNCAO |
| Turno | SR6 | R6\_TURNO |
| Sindicato | RCE | RCE\_CODIGO |
| Filial | SM0 | M0\_CODFIL |
| Cliente\* | SA1 | A1\_COD |
| Local de trabalho\* | ABS | ABS\_LOCAL |
| Turno do Posto\* | TDX | TDX\_COD |

**Atenção:** As entidades **Cliente, Local de trabalho** e **Turno do Posto** só estarão disponíveis no cadastro se a integração com o **Gestão de Serviços, SIGATEC,** estiver habilitada com o parâmetro **MV\_TECXRH**.   
  
  
**Importante:** Só é possível ter **um** **critério** **ativo** para uma filial em um mesmo período. Caso seja necessário cadastrar um critério diferente será necessário alterar o status para **Inativo**, ou alterar o período final.

Acesse o **Manual do Cálculo Automático [aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=557350063)**  
  
  
  
**Saiba Mais**[RH - Linha Protheus - GPE - Como é feito o cálculo automático de benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhCeYrTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzMTM1MzE1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby0lQzMlQTktZmVpdG8tby1jJUMzJUExbGN1bG8tYXV0b20lQzMlQTF0aWNvLWRlLWJlbmVmJUMzJUFEY2lvcwY7CFQ6DnNlYXJjaF9pZEkiKTU0NTg1Mzk5LWYwN2QtNGVlNy04ZWQyLWQ3OWZmMWQyNjI5ZAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiOENvbW8gw6kgZmVpdG8gbyBjw6FsY3VsbyBhdXRvbcOhdGljbyBkZSBiZW5lZsOtY2lvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--e6a821c2393c856c678f27e531b4ebb4e8b225cd)  
[RH - Linha Protheus - GPE - Relatório de Conferência para Cálculo de Benefícios Automáticos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj6I8fUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjEwNjIzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUmVsYXQlQzMlQjNyaW8tZGUtQ29uZmVyJUMzJUFBbmNpYS1wYXJhLUMlQzMlQTFsY3Vsby1kZS1CZW5lZiVDMyVBRGNpb3MtQXV0b20lQzMlQTF0aWNvcwY7CFQ6DnNlYXJjaF9pZEkiKTU0NTg1Mzk5LWYwN2QtNGVlNy04ZWQyLWQ3OWZmMWQyNjI5ZAY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiOENvbW8gw6kgZmVpdG8gbyBjw6FsY3VsbyBhdXRvbcOhdGljbyBkZSBiZW5lZsOtY2lvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--e318729786578624c8765c6fa878cedcd66250d6)  
[RH - Linha Protheus - GPE - No cálculo automático de benefícios, o sistema faz o cálculo normalmente mesmo que não haja vínculo para receber benefício.](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiRCsbUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB%2BWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjAzNDE5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTm8tYyVDMyVBMWxjdWxvLWF1dG9tJUMzJUExdGljby1kZS1iZW5lZiVDMyVBRGNpb3Mtby1zaXN0ZW1hLWZhei1vLWMlQzMlQTFsY3Vsby1ub3JtYWxtZW50ZS1tZXNtby1xdWUtbiVDMyVBM28taGFqYS12JUMzJUFEbmN1bG8tcGFyYS1yZWNlYmVyLWJlbmVmJUMzJUFEY2lvLQY7CFQ6DnNlYXJjaF9pZEkiKTU0NTg1Mzk5LWYwN2QtNGVlNy04ZWQyLWQ3OWZmMWQyNjI5ZAY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiOENvbW8gw6kgZmVpdG8gbyBjw6FsY3VsbyBhdXRvbcOhdGljbyBkZSBiZW5lZsOtY2lvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--f6cc9e49d0b42b28a7924c22ec4e40cdcd07eafe)
