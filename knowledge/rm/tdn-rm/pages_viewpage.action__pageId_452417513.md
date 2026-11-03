---
content_hash: 724d7db3a004fd2488283830f265c9e68e7b7e7ec1013f7d03de195c642ae0fc
fetched_at: '2026-06-29T00:09:58.309335+00:00'
page_id: '452417513'
product: rm
source: tdn-rm
title: Atualizações para atender o eSocial - Leiaute 2.5
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452417513
version: 11
---

**Releases: 12.1.21.200, 12.1.22.169 e 12.1.23.105 ou superiores.**

**ATENÇÃO:**

Para liberação da adequação ao leiaute 2.5 do eSocial, foram criados campos em alguns cadastros da Folha de Pagamento e Segurança Medicina do Trabalho. A partir dos patchs 12.1.21.200, 12.1.22.169 e 12.1.23.105, será OBRIGATÓRIO a execução do Atualizador para acessar esses módulos. 

Observação: Para segurança das informações, sugerimos que o processo seja executado primeiramente em ambiente de **homologação.**

Caso tenha dúvidas sobre a execução desse Script via RM.Atualizador, acesse: <http://tdn.totvs.com/pages/releaseview.action?pageId=322143046>

# Alterações contempladas:

S-1000

* Criação do campo "Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária" no cadastro de informações do empregador;
* Ajustes na geração do XML do campo IndOpcCP nas informações do Empregador.

S-1020

* Ajustado o evento S-1020 quando o layout for igual a 2.5 verificar o tipo de classificação tributaria.

S-2200

* Alterada validação do campo dtNascto do grupo dependente para: Deve ser maior ou igual que 01/01/1890 e menor que a data atual;

* Incluída validação na geração do XML, sobre a obrigatoriedade do campo cpfDep do grupo dependente;
* Incluído campo "Tipo de contrato por prazo determinado" no cadastro de funcionário na aba Registro I Dados do Contrato;
* Incluído campo "Motivo da contratação por prazo determinado" no cadastro de funcionário na aba Registro I Dados do Contrato;
* Ajuste na geração do XML para considerar as informações do novo tipo de contrato por tempo determinado;
* Alterada validação para o campo caluAssec do grupo duração: "O preenchimento é obrigatório se {tpContr} = [2, 3]. Não preencher se {tpContr} = [1].";
* Ajuste na geração do XML para considerar o campo tpInscAnt no grupo sucessaoVinc.

S-2230

* Ajuste na geração do evento S-2230 para validar o campo {origRetif} para gerar a tag 'codCid'

S-2298

* Inclusão de validação na tag nrProcJud do grupo infoReintegr. Se preenchido deve ser processo judicial com 20 algarismos.

S-2299

* Incluída validação na geração do XML, sobre a obrigatoriedade do campo cpfDep do grupo detPlano.
* Alterada validação do campo nrProcTrab do grupo infoDeslig: "Se preenchido, deve ser um processo judicial válido, com 20 (vinte) algarismos."
* Criação do campo tpInscSuc no grupo sucessaoVinc na geração do XML.

S-2300

* Incluída a validação na geração do XML: Se {cadIni} = [S], deve ser anterior à data de início da obrigatoriedade dos eventos não periódicos para o empregador;"

S-2399

* Criado os campos pensAlim, percAliment e vrAlim no grupo infoTSVTermino;
* Incluída validação na geração do XML, sobre a obrigatoriedade do campo cpfDep do grupo detPlano.

S-1250

* Criação do campo indOpcCP no  grupo ideProdutor na geração do XML;
* Campos dos grupos {tpAquis}, {ideProdutor}, {nfs} e {infoProcJud} - elementos alterados para "A"(atributo).

S-1210

* Alterada validação do campo dtNasctoBenef do grupo penAlim para: Deve ser maior ou igual que 01/01/1890 e menor que a data atual.

# Eventos de SST

**Atenção:** Esses eventos estão disponíveis apenas para geração no Totvs Folha de Pagamento nos ambientes de Homologação e Produção Restrita.

Ajustes para atendimento ao leiaute 2.5:

S-1060: [http://tdn.totvs.com/pages/viewpage.action?pageId=452396260](https://www.google.com/url?q=http://tdn.totvs.com/pages/viewpage.action?pageId%3D452396260&sa=D&source=hangouts&ust=1547902836016000&usg=AFQjCNGwKybzSkqwTtZAXWJUL9kIr9cd1A)

S-2210: [http://tdn.totvs.com/pages/viewpage.action?pageId=364908460](https://www.google.com/url?q=http://tdn.totvs.com/pages/viewpage.action?pageId%3D364908460&sa=D&source=hangouts&ust=1547902836016000&usg=AFQjCNHgN7o96FuQjyMMv712QyXC10d9ig)

S-2220: [http://tdn.totvs.com/pages/viewpage.action?pageId=364908475](https://www.google.com/url?q=http://tdn.totvs.com/pages/viewpage.action?pageId%3D364908475&sa=D&source=hangouts&ust=1547902836017000&usg=AFQjCNG2OsjAg7P8MLlOQPZJwizhE95-MA)

S-2245: <http://tdn.totvs.com/pages/viewpage.action?pageId=398753796>
